import os

from google.adk.models.lite_llm import LiteLlm


def get_model():
    provider = os.getenv("MODEL_PROVIDER", "local").lower()

    if provider == "local":
        local_model = os.getenv("LOCAL_MODEL", "ollama_chat/gemma3:latest")
        return LiteLlm(model=local_model)

    if provider == "google":
        return os.getenv("GOOGLE_MODEL", "gemini-flash-latest")

    raise ValueError("MODEL_PROVIDER deve ser 'local' ou 'google'")