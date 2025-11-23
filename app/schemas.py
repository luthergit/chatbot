from typing import List, Optional, Literal, Dict, Any, TypedDict
from pydantic import BaseModel, Field

Role = Literal["system", "user", "assistant", "tool"]

class ChatState(TypedDict, total=False):
    messages: List[Dict[str, Any]]
    reply: str

class ChatMessage(BaseModel):
    role: Role
    content: str = Field(..., min_length=1)

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    history: Optional[List[ChatMessage]] = None
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    stream: Optional[bool] = None

class Usage(BaseModel):
    prompt_tokens: Optional[int] = None
    completion_tokens: Optional[int] = None
    total_tokens: Optional[int] = None
    cost: Optional[float] = None

class ChatResponse(BaseModel):
    reply: str
    model: Optional[str] = None
    finish_reason: Optional[str] = None
    usage: Optional[Usage] = None 

class ReasoningRequest(BaseModel):
    message: str

class ReasoningEnqueueResponse(BaseModel):
    job_id: str

class ReasoningStatusResponse(BaseModel):
    status: str
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None