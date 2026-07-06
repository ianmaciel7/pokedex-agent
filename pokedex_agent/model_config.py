import os

from google.adk.models.lite_llm import LiteLlm


def get_model():
    provider = os.getenv("MODEL_PROVIDER", "local").lower()

    if provider == "local":
        # Force-override GOOGLE_API_KEY to a dummy value so ADK cannot
        # authenticate with Google even if .env loaded a real key first.
        os.environ["GOOGLE_API_KEY"] = "dummy"
        local_model = os.getenv("LOCAL_MODEL", "ollama_chat/qwen3:4b")
        return LiteLlm(model=local_model)

    if provider == "google":
        return os.getenv("GOOGLE_MODEL", "gemini-flash-latest")

    raise ValueError("MODEL_PROVIDER deve ser 'local' ou 'google'")