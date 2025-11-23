from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, END
from app.clients.openrouter import chat_completion
from app.config import settings

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from app.schemas import ChatState

def with_system_prompt(messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not any(m.get("role") == "system" for m in messages):
        messages = [{"role": "system", "content": settings.system_prompt}] + messages
    return messages

def to_lc_messages(messages: List[Dict[str,Any]]) -> List[Dict[str,Any]]:
    out = []
    for m in messages:
        role = m.get("role")
        content = m.get("content", "")
        if role == "system":
            out.append(SystemMessage(content=content))
        elif role == "user":
            out.append(HumanMessage(content=content))
        elif role == "assistant":
            out.append(AIMessage(content=content))

    return out
# _llm = ChatOpenAI(api_key=settings.openrouter_api_key,
#                   base_url=settings.openrouter_base_url,
#                   model=settings.openrouter_model,
#                   temperature=settings.temperature,
#                   max_tokens=settings.max_tokens,
#                   streaming = True)

# class ChatState(TypedDict, total=False):
#     messages: List[Dict[str, Any]]
#     reply: str

def build_graph(
        model: str | None = None,
        temperature: float | None = None,
        max_tokens: int | None = None,
        streaming: bool = True,
        ):
    model_name = model or settings.openrouter_model
    temperature = temperature if temperature is not None else settings.temperature
    max_tokens = max_tokens if max_tokens is not None else settings.max_tokens

    llm = ChatOpenAI(api_key=settings.openrouter_api_key,
                     base_url=settings.openrouter_base_url,
                     model=model_name,
                     temperature=temperature,
                     max_tokens=max_tokens,
                     streaming=streaming)

    async def llm_node(state: ChatState) -> ChatState:
        messages = state.get("messages", [])
        # Ensure a system prompt is present
        messages = with_system_prompt(messages)
        lc_msgs = to_lc_messages(messages)

        result = await llm.ainvoke(lc_msgs)
        reply_text = result.content or ""
        messages = messages + [{"role": "assistant", "content": reply_text}]

        return {"messages": messages, "reply": reply_text}


    graph = StateGraph(ChatState)
    graph.add_node("llm", llm_node)
    graph.set_entry_point("llm")
    graph.add_edge("llm", END)
    return graph.compile() 