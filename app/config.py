import os

class Settings:
    def __init__(self) -> None:
        self.app_url = os.environ.get("APP_URL", "http://127.0.0.1:8001")
        self.app_name = os.environ.get("APP_NAME", "Chatbot (OpenRouter)")
        self.openrouter_api_key = os.environ.get("OPENROUTER_API_KEY", "")
        self.openrouter_base_url = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
        self.openrouter_model = os.environ.get("OPENROUTER_MODEL", "openrouter/auto")
        self.temperature = float(os.environ.get("OPENROUTER_TEMPERATURE", "0.2"))
        self.max_tokens = int(os.environ.get("OPENROUTER_MAX_TOKENS", "512"))
        self.system_prompt = os.environ.get("SYSTEM_PROMPT", "You are a concise, helpful assistant.")

    def require_api_key(self) -> None:
        if not self.openrouter_api_key:
            raise RuntimeError("OPENROUTER_API_KEY is not set")

settings = Settings() 