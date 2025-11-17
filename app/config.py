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
        self.session_secret = os.environ.get("SESSION_SECRET", "chatbot-change-me")
        self.session_max_age = int(os.environ.get("SESSION_MAX_AGE", "3600"))
        self.session_cookie_name = os.environ.get("SESSION_COOKIE_NAME", "session")
        self.session_cookies_secure = os.environ.get("SESSION_COOKIES_SECURE", "true").lower() == "true"
        self.session_cookies_samesite = os.environ.get("SESSION_COOKIES_SAMESITE", "none")
        self.streaming_enabled = os.environ.get("STREAMING_ENABLED", "false").lower() == "true"

        origins = os.environ.get("ALLOWED_ORIGINS")
        self.cors_allow_origins = [o.strip() for o in origins.split(",") if o.strip()]
        
        raw_users = os.environ.get("BASIC_USERS")

        users = {}
        for pair in raw_users.split(","):
            pair = pair.strip()

            if not pair or ':' not in pair:
                continue
            user, pwd = pair.split(":", 1)

            users[user.strip()] = pwd.strip()
        self.basic_users = users
        self.max_history = int(os.environ.get("MAX_HISTORY"))


    def require_api_key(self) -> None:
        if not self.openrouter_api_key:
            raise RuntimeError("OPENROUTER_API_KEY is not set")

settings = Settings() 