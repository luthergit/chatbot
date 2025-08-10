# Chatbot (FastAPI + LangGraph + OpenRouter)

- Run: `uv sync` then `uv run uvicorn app.main:app --reload`
- Set environment in `.env` as in `.env.example`.
- Endpoint: `POST /chat` body: `{ "message": "Hello" }`
- Health: `GET /health`

Requirements: Python 3.11+, `uv` installed. 