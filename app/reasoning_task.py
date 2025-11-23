import asyncio
from typing import List, Dict, Any
from app.chat_graph import build_graph
from app.config import settings

_graph = build_graph(
    model=settings.reasoning_model,
    temperature=settings.temperature,
    max_tokens=settings.reasoning_max_tokens,
    streaming=False
)

async def _run(messages: List[Dict[str, Any]]) -> Dict[str, Any]:
    state = {"messages": messages}
    result = await _graph.ainvoke(state)
    reply = result.get("reply", "")
    return {"reply": reply}

def run_reasoning(messages: List[Dict[str, Any]]) -> Dict[str, Any]:
    return asyncio.run(_run(messages))