"""Shared helpers for building root and specialist agents."""

from collections.abc import Callable

from google.adk.agents.llm_agent import Agent, LlmAgent
from google.adk.models.base_llm import BaseLlm
from google.adk.models.registry import LLMRegistry
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.base_toolset import BaseToolset
from pydantic import Field

from pokedex_agent.model_config import get_live_model, get_model

type AgentTool = Callable[..., str] | BaseTool | BaseToolset

IMAGE_RESPONSE_INSTRUCTION = (
    "When returning information about a specific Pokémon, item, berry, or other "
    "entity with an available visual equivalent, include one relevant image near "
    "the top of the answer using Markdown image syntax. Use tool-provided image "
    "URLs when available. Do not invent image URLs; if no relevant image is "
    "available, continue without one."
)

POKEDEX_VOICE_INSTRUCTION = (
    "Speak with the concise, electronic field-guide style of the anime Pokédex: "
    "calm, precise, encyclopedic, and trainer-facing. Start direct factual answers "
    "with a compact scan-style summary when useful, then give the requested data "
    "in short, readable lines. Prefer verified facts from tools over speculation. "
    "Keep the tone lightly helpful rather than chatty, dramatic, or overly cute. "
    "Do not imitate copyrighted episode dialogue; create original wording."
)


class PokedexAgent(LlmAgent):
    live_model: BaseLlm | str = Field(default_factory=get_live_model)

    @property
    def canonical_live_model(self) -> BaseLlm:
        if isinstance(self.live_model, BaseLlm):
            return self.live_model
        return LLMRegistry.new_llm(self.live_model)


def create_sub_agent(
    name: str, description: str, instruction: str, tools: list[AgentTool]
) -> Agent:
    return PokedexAgent(
        model=get_model(),
        live_model=get_live_model(),
        name=name,
        description=description,
        instruction=(
            f"{instruction} {POKEDEX_VOICE_INSTRUCTION} {IMAGE_RESPONSE_INSTRUCTION}"
        ),
        tools=tools,
    )


def create_root_agent(
    name: str, description: str, instruction: str, sub_agents: list[Agent]
) -> Agent:
    return PokedexAgent(
        model=get_model(),
        live_model=get_live_model(),
        name=name,
        description=description,
        instruction=(
            f"{instruction} {POKEDEX_VOICE_INSTRUCTION} {IMAGE_RESPONSE_INSTRUCTION}"
        ),
        sub_agents=sub_agents,
    )
