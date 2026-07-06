import os
from typing import AsyncGenerator

from google.adk.models.base_llm import BaseLlm
from google.adk.models.lite_llm import LiteLlm
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.genai import types


class ConfigurationErrorLlm(BaseLlm):
    error_message: str

    async def generate_content_async(
        self, llm_request: LlmRequest, stream: bool = False
    ) -> AsyncGenerator[LlmResponse, None]:
        text = (
            f"Configuration error: {self.error_message}\n\n"
            "Fix the selected environment file, then restart ADK Web."
        )
        yield LlmResponse(
            content=types.Content(
                role="model",
                parts=[types.Part.from_text(text=text)],
            ),
            partial=False,
        )


def _configuration_error(message: str) -> ConfigurationErrorLlm:
    return ConfigurationErrorLlm(model="configuration-error", error_message=message)


def _google_model_name():
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

    if not api_key or api_key == "dummy":
        return _configuration_error(
            "MODEL_PROVIDER=google requires a valid Gemini API key in the "
            "selected environment file. "
            "Set GOOGLE_API_KEY or GEMINI_API_KEY."
        )

    if api_key.startswith("REPLACE_WITH_") or api_key == "your-google-ai-studio-api-key":
        return _configuration_error(
            "Replace the placeholder API key in the selected environment file "
            "with a real Gemini API key from Google AI Studio. Editing "
            ".env.example is not enough."
        )

    if api_key.startswith("ya29."):
        return _configuration_error(
            "GOOGLE_API_KEY looks like an OAuth access token. Use a Gemini API "
            "key from Google AI Studio instead."
        )

    os.environ["GOOGLE_API_KEY"] = api_key
    return os.getenv("GOOGLE_MODEL", "gemini-flash-latest")


def get_model():
    provider = os.getenv("MODEL_PROVIDER", "local").lower()

    if provider == "local":
        # Force-override GOOGLE_API_KEY to a dummy value so ADK cannot
        # authenticate with Google even if an env file loaded a real key first.
        os.environ["GOOGLE_API_KEY"] = "dummy"
        local_model = os.getenv("LOCAL_MODEL", "ollama_chat/qwen3:4b")
        return LiteLlm(model=local_model)

    if provider == "google":
        return _google_model_name()

    return _configuration_error("MODEL_PROVIDER must be 'local' or 'google'.")
