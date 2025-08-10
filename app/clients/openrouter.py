from typing import List, Dict, Any, Optional
import httpx
from fastapi import HTTPException
from app.config import settings

async def chat_completion(
    messages: List[Dict[str, Any]],
    model: Optional[str] = None,
    temperature: Optional[float] = None,
    max_tokens: Optional[int] = None,
) -> Dict[str, Any]:
    if not settings.openrouter_api_key:
        raise HTTPException(status_code=500, detail="OPENROUTER_API_KEY not configured")

    url = f"{settings.openrouter_base_url.rstrip('/')}/chat/completions"

    headers = {
        "Authorization": f"Bearer {settings.openrouter_api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": settings.app_url,
        "X-Title": settings.app_name,
    }

    payload_model = model or settings.openrouter_model
    payload_temp = settings.temperature if temperature is None else temperature
    payload_max = settings.max_tokens if max_tokens is None else max_tokens

    payload: Dict[str, Any] = {
        "model": payload_model,
        "messages": messages,
        "temperature": payload_temp,
        "max_tokens": payload_max,
        "usage": {"include": True},
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(url, headers=headers, json=payload)

    if resp.status_code >= 400:
        try:
            data = resp.json()
            message = data.get("error", {}).get("message") or data
        except Exception:
            message = resp.text
        raise HTTPException(status_code=resp.status_code, detail=f"OpenRouter error: {message}")

    data = resp.json()
    try:
        choice = data["choices"][0]
        if "message" in choice and choice["message"] is not None:
            content = choice["message"]["content"] or ""
        elif "text" in choice:
            content = choice["text"] or ""
        else:
            content = ""
        usage = data.get("usage") or {}
        finish_reason = choice.get("finish_reason")
        model_used = data.get("model")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected OpenRouter response schema: {e}")

    return {
        "content": content,
        "usage": usage,
        "finish_reason": finish_reason,
        "model": model_used,
    } 