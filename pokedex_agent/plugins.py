"""Application-wide ADK plugins."""

import logging
from typing import Any

from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.adk.plugins.base_plugin import BasePlugin
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext
from google.genai import types

logger = logging.getLogger(__name__)


def _is_resource_exhausted_error(error: Exception) -> bool:
    error_name = type(error).__name__.lower()
    error_text = str(error).lower()
    return "resourceexhausted" in error_name or "resource exhausted" in error_text


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
        tool_args: dict[str, Any],
        tool_context: ToolContext,
        error: Exception,
    ) -> dict[str, Any]:
        logger.exception(
            "Tool error in agent %s while running %s with args %s",
            tool_context.agent_name,
            tool.name,
            tool_args,
            exc_info=error,
        )
        return {
            "ok": False,
            "error": type(error).__name__,
            "message": (
                f"The tool '{tool.name}' failed while fetching Pokémon data. "
                "Ask the user to retry or provide a more specific identifier."
            ),
        }
