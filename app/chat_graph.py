from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, END
from app.clients.openrouter import chat_completion
from app.config import settings

class ChatState(TypedDict, total=False):
    messages: List[Dict[str, Any]]
    reply: str

async def llm_node(state: ChatState) -> ChatState:
    messages = state.get("messages", [])
    # Ensure a system prompt is present
    if not any(m.get("role") == "system" for m in messages):
        messages = [{"role": "system", "content": settings.system_prompt}] + messages

    result = await chat_completion(messages=messages)
    reply_text = result["content"]
    messages = messages + [{"role": "assistant", "content": reply_text}]

    return {"messages": messages, "reply": reply_text}

def build_graph():
    graph = StateGraph(ChatState)
    graph.add_node("llm", llm_node)
    graph.set_entry_point("llm")
    graph.add_edge("llm", END)
    return graph.compile() 