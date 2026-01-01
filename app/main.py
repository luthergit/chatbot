import json
from dotenv import load_dotenv
load_dotenv()

from app.config import settings 
from fastapi import FastAPI, Depends, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.schemas import ChatRequest, ChatResponse, ReasoningRequest, ReasoningEnqueueResponse, ReasoningStatusResponse
from app.chat_graph import build_graph, ChatState
from app.storage import init_db, close_db, load_messages, save_message
from app.auth import _create_session_token, get_current_user_cookie, verify_user_password
from starlette.responses import StreamingResponse
from app.observability import observe, lf_handler

from app.queue import enqueue_reasoning, get_job
from typing import Dict, Any


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    try:
        yield
    finally:
        await close_db()

app = FastAPI(title="Chatbot (OpenRouter + FastAPI + LangGraph)", version="0.1.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_methods=['GET', 'POST', 'OPTIONS'],
    allow_headers=['Content-Type', 'Authorization'],
    allow_credentials=True
)

graph = build_graph()

from pydantic import BaseModel
class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(req: LoginRequest, response: Response) -> dict:
    if not verify_user_password(req.username, req.password):
        return Response(status_code=401)
    token = _create_session_token(req.username)
    response.set_cookie(key=settings.session_cookie_name, 
                        value=token, httponly=True, 
                        secure=settings.session_cookies_secure,
                        max_age=settings.session_max_age,
                        samesite=settings.session_cookies_samesite, path="/")
    return {"ok": True}

@app.post("/logout")
async def logout(response: Response) -> dict:
    response.delete_cookie(key=settings.session_cookie_name, path="/")
    return {"ok": True}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/session")
async def session(user: str = Depends(get_current_user_cookie)) -> dict:
    return {'user': user}

@app.post("/chat")
async def chat(req: ChatRequest, user: str = Depends(get_current_user_cookie)) -> ChatResponse:
    use_stream = bool(settings.streaming_enabled and req.stream)

    messages = await load_messages(user, limit=settings.max_history)
    messages.append({"role": "user", "content": req.message})

    if not use_stream:

        state: ChatState = {"messages": messages}
        result: ChatState = await graph.ainvoke(state, 
                                                config={"callbacks":[lf_handler], "metadata": {"langfuse_user_id": user},
                                                       "run_name": "chat"})

        reply = result.get("reply", "")
        await save_message(user, "user", req.message)
        await save_message(user, "assistant", reply)

        return ChatResponse(
            reply=reply,
            model=None,
            finish_reason=None,
            usage=None,
        )

    await save_message(user, "user", req.message)
    state: ChatState = {"messages": messages}

    async def event_gen():
        chunks = []

        try:
            async for event in graph.astream_events(
                state,
                version="v1",
                config={"callbacks":[lf_handler], "metadata": {"langfuse_user_id": user}, "run_name": "chat"},
                # include_types=['on_chat_model_stream', "on_llm_stream"]
            ):
                # print("EV:", event.get("event"))
                ev = event.get("event")
                if ev in ('on_chat_model_stream', "on_llm_stream"):
                    data = event.get("data") or {}
                    chunk = data.get("chunk")
                    if hasattr(chunk, 'content'): #or data.get("token") or data.get("output"):
                        delta = chunk.content or ""
                        if delta:
                            chunks.append(delta)
                            yield f"data: {json.dumps({'delta': delta})}\n\n"
            
            full = "".join(chunks)
            await save_message(user, "assistant", full)
            yield "data: [DONE]\n\n"
        except Exception as e:
            yield f"event: error\ndata: {json.dumps({'message': str(e)})}\n\n"

        
    return StreamingResponse(event_gen(), media_type="text/event-stream", headers={
        "Cache-Control": "no-cache",
        "X-Accel-Buffering": "no",  # helps if behind nginx in future
        "Connection": "keep-alive",
    })



@app.post("/reasoning", response_model=ReasoningEnqueueResponse)
async def reasoning(req: ReasoningRequest, user: str = Depends(get_current_user_cookie)) -> Dict[str, Any]:
    messages = await load_messages(user, limit=settings.max_history)
    messages.append({'role': 'user', 'content': req.message})

    await save_message(user, 'user', req.message)

    job = enqueue_reasoning(messages, user)
    return {'job_id': job.get_id()}

@app.get("/reasoning/{job_id}", response_model=ReasoningStatusResponse)
async def reasoning_status(job_id:str, user: str = Depends(get_current_user_cookie)) -> Dict[str, Any]:
    try:
        job = get_job(job_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail= 'Job not found')
    
    status = job.get_status(refresh=True)

    if status == 'finished':
        result = job.result or {}

        saved = job.meta.get('saved')
        if not saved and isinstance(result, dict) and 'reply' in result:
            await save_message(user, 'assistant', result['reply'])
            job.meta['saved'] = True
            job.save_meta()
        return {'status': 'finished', 'result': result}
    
    elif status == 'failed':
        err = job.exc_info or 'Job failed'
        return {'status': 'failed', 'error':err}
    
    return {'status': status}

