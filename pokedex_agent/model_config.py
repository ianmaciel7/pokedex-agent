import os
import asyncio
from typing import AsyncGenerator, AsyncIterator

from google.adk.models.base_llm import BaseLlm
from google.adk.models.base_llm_connection import BaseLlmConnection
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


class UnsupportedLiveConnection(BaseLlmConnection):
    def __init__(self, message: str) -> None:
        self._closed = asyncio.Event()
        self._message = message
        self._warned = False

    async def __aenter__(self) -> "UnsupportedLiveConnection":
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        await self.close()

    async def _warn_once(self) -> None:
        self._warned = True

    async def send_history(self, history: list[types.Content]) -> None:
        if history and history[-1].role == "user":
            await self._warn_once()

    async def send_content(self, content: types.Content) -> None:
        await self._warn_once()

    async def send_realtime(self, blob: types.Blob) -> None:
        await self._warn_once()

    async def receive(self) -> AsyncIterator[LlmResponse]:
        while not self._closed.is_set():
            if self._warned:
                self._warned = False
                yield LlmResponse(
                    content=types.Content(
                        role="model",
                        parts=[types.Part.from_text(text=self._message)],
                    ),
                    partial=False,
                )
            await asyncio.sleep(0.1)

    async def close(self) -> None:
        self._closed.set()


class UnsupportedLiveLlm(BaseLlm):
    message: str

    async def generate_content_async(
        self, llm_request: LlmRequest, stream: bool = False
    ) -> AsyncGenerator[LlmResponse, None]:
        yield LlmResponse(
            content=types.Content(
                role="model",
                parts=[types.Part.from_text(text=self.message)],
            ),
            partial=False,
        )

    def connect(self, llm_request: LlmRequest) -> UnsupportedLiveConnection:
        return UnsupportedLiveConnection(self.message)


def _configuration_error(message: str) -> ConfigurationErrorLlm:
    return ConfigurationErrorLlm(model="configuration-error", error_message=message)


def _google_model_name() -> BaseLlm | str:
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key or api_key == "dummy":
        return _configuration_error(
            "MODEL_PROVIDER=google requires a valid Gemini API key in the "
            "selected environment file. "
            "Set GOOGLE_API_KEY."
        )

    if (
        api_key.startswith("REPLACE_WITH_")
        or api_key == "your-google-ai-studio-api-key"
    ):
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
    return os.getenv("GOOGLE_MODEL", "gemini-2.5-flash-latest")


def _nvidia_model() -> BaseLlm:
    api_key = os.getenv("NVIDIA_NIM_API_KEY") or os.getenv("NVIDIA_API_KEY")

    if not api_key or api_key.startswith("REPLACE_WITH_"):
        return _configuration_error(
            "MODEL_PROVIDER=nvidia requires a valid NVIDIA NIM API key in the "
            "selected environment file. Set NVIDIA_NIM_API_KEY."
        )

    os.environ["NVIDIA_NIM_API_KEY"] = api_key
    model = os.getenv(
        "NVIDIA_MODEL",
        "nvidia_nim/deepseek-ai/deepseek-v4-flash",
    )
    reasoning_effort = os.getenv("NVIDIA_REASONING_EFFORT", "none")
    return LiteLlm(
        model=model,
        extra_body={"reasoning_effort": reasoning_effort},
    )


def get_model() -> BaseLlm | str:
    provider = os.getenv("MODEL_PROVIDER", "local").lower()

    if provider == "local":
        # Force-override GOOGLE_API_KEY to a dummy value so ADK cannot
        # authenticate with Google even if an env file loaded a real key first.
        os.environ["GOOGLE_API_KEY"] = "dummy"
        local_model = os.getenv("LOCAL_MODEL", "ollama_chat/qwen3:4b")
        return LiteLlm(model=local_model)

    if provider == "google":
        return _google_model_name()

    if provider == "nvidia":
        return _nvidia_model()

    return _configuration_error(
        "MODEL_PROVIDER must be 'local', 'google', or 'nvidia'."
    )


def get_live_model() -> BaseLlm | str:
    provider = os.getenv("MODEL_PROVIDER", "local").lower()

    if provider == "google":
        return os.getenv(
            "GOOGLE_LIVE_MODEL",
            "gemini-2.5-flash-native-audio-preview-12-2025",
        )

    configured_model = getattr(get_model(), "model", provider)
    return UnsupportedLiveLlm(
        model=configured_model,
        message=(
            f"Live mode is not supported for {configured_model}. Use the normal "
            "ADK Web text chat with this model, or switch MODEL_PROVIDER=google "
            "and set GOOGLE_LIVE_MODEL to a Gemini Live model before using the "
            "audio/video live controls."
        ),
    )
