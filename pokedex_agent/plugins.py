"""Application-wide ADK plugins."""

import logging
from collections.abc import Mapping

from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.adk.plugins.base_plugin import BasePlugin
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext
from google.genai import types
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class ToolErrorResponse(BaseModel):
    """Structured response payload for plugin-level tool errors."""

    input: dict[str, object]
    error: str


def _is_resource_exhausted_error(error: Exception) -> bool:
    error_name = type(error).__name__.lower()
    error_text = str(error).lower()
    return "resourceexhausted" in error_name or "resource exhausted" in error_text


def _is_authentication_error(error: Exception) -> bool:
    error_name = type(error).__name__.lower()
    error_text = str(error).lower()
    return "authentication" in error_name or "unauthorized" in error_text


def _is_mid_stream_error(error: Exception) -> bool:
    error_name = type(error).__name__.lower()
    error_text = str(error).lower()
    return "midstream" in error_name or "mid-stream" in error_text


def _is_unsupported_params_error(error: Exception) -> bool:
    error_name = type(error).__name__.lower()
    return "unsupportedparams" in error_name


class GlobalErrorPlugin(BasePlugin):
    """Provide graceful fallback responses for unhandled model and tool errors."""

    def __init__(self) -> None:
        super().__init__(name="global_error")

    async def on_model_error_callback(
        self,
        *,
        callback_context: CallbackContext,
        llm_request: LlmRequest,
        error: Exception,
    ) -> LlmResponse:
        logger.exception(
            "Model error in agent %s",
            callback_context.agent_name,
            exc_info=error,
        )
        if _is_resource_exhausted_error(error):
            text = (
                "The selected model quota or rate limit was exhausted while "
                "handling that request. Wait a moment and retry, switch to the "
                "local model profile, or use a Gemini API key/project with "
                "available quota."
            )
            error_message = "Model quota or rate limit exhausted."
        elif _is_authentication_error(error):
            text = (
                "The selected model rejected the API credentials. Check that "
                "the active environment file contains a valid API key for the "
                "selected provider, then restart ADK Web. For NVIDIA NIM, use "
                "NVIDIA_NIM_API_KEY with a key that starts with 'nvapi-'."
            )
            error_message = "Model authentication failed."
        elif _is_mid_stream_error(error):
            text = (
                "The selected model failed while streaming the response. "
                "Retry the request. If this happens with NVIDIA NIM, set "
                "NVIDIA_REASONING_EFFORT=none in the active environment file "
                "and restart ADK Web."
            )
            error_message = "Model failed during streaming."
        elif _is_unsupported_params_error(error):
            text = (
                "The selected model provider rejected one of the configured "
                "model parameters. Check provider-specific settings in the "
                "active environment file and restart ADK Web."
            )
            error_message = "Model provider rejected configured parameters."
        else:
            text = (
                "I hit an internal model error while handling that request. "
                "Please try again in a moment."
            )
            error_message = "Unhandled model error handled by GlobalErrorPlugin."

        return LlmResponse(
            content=types.Content(
                role="model",
                parts=[types.Part.from_text(text=text)],
            ),
            error_code=type(error).__name__,
            error_message=error_message,
        )

    async def on_tool_error_callback(
        self,
        *,
        tool: BaseTool,
        tool_args: Mapping[str, object],
        tool_context: ToolContext,
        error: Exception,
    ) -> dict[str, object]:
        logger.exception(
            "Tool error in agent %s while running %s with args %s",
            tool_context.agent_name,
            tool.name,
            tool_args,
            exc_info=error,
        )
        payload = ToolErrorResponse(
            input=dict(tool_args),
            error=(
                f"{type(error).__name__}: "
                f"The tool failed while fetching Pokémon data. "
                "Ask the user to retry or provide a more specific identifier."
            ),
        )
        return payload.model_dump()
