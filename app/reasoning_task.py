import asyncio
from typing import List, Dict, Any
from app.chat_graph import build_graph
from app.config import settings
from app.observability import lf_handler, observe, langfuse
from rq import get_current_job

_graph = build_graph(
    model=settings.reasoning_model,
    temperature=settings.temperature,
    max_tokens=settings.reasoning_max_tokens,
    streaming=False
)

async def _run(messages: List[Dict[str, Any]], user: str | None) -> Dict[str, Any]:
    job = get_current_job()
    job_id = job.id if job else None


    state = {"messages": messages}
    result = await _graph.ainvoke(state,
                                  config={"callbacks":[lf_handler], "metadata": {"job_id": job_id}, 
                                          "langfuse_user_id": user,
                                          "run_name": "reasoning"})
    reply = result.get("reply", "")
    return {"reply": reply}


def run_reasoning(messages: List[Dict[str, Any]], user: str | None = None) -> Dict[str, Any]:
    res = asyncio.run(_run(messages, user))
    langfuse.flush()  # ensure worker sends before job ends
    return res