
from dotenv import load_dotenv
load_dotenv()

from app.config import settings 
from fastapi import FastAPI, Depends
from app.auth import get_current_user
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import ChatRequest, ChatResponse
from app.chat_graph import build_graph, ChatState
from app.storage import init_db, close_db, load_messages, save_message

app = FastAPI(title="Chatbot (OpenRouter + FastAPI + LangGraph)", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_methods=['POST', 'OPTIONS'],
    allow_headers=['Content-Type', 'Authorization']
)
@app.on_event("startup")
async def startup():
    await init_db()

@app.on_event("shutdown")
async def shutdown():
    await close_db()

graph = build_graph()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest, user: str = Depends(get_current_user)) -> ChatResponse:
    messages = await load_messages(user, limit=settings.max_history)

    messages.append({"role": "user", "content": req.message})

    state: ChatState = {"messages": messages}
    result: ChatState = await graph.ainvoke(state)

    reply = result.get("reply", "")
    await save_message(user, "user", req.message)
    await save_message(user, "assistant", reply)

    return ChatResponse(
        reply=reply,
        model=None,
        finish_reason=None,
        usage=None,
    ) 