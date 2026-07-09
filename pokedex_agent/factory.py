"""Shared helpers for building root and specialist agents."""

from collections.abc import Callable
from collections.abc import Mapping

from google.adk.agents.llm_agent import Agent, LlmAgent
from google.adk.models.base_llm import BaseLlm
from google.adk.models.registry import LLMRegistry
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.base_toolset import BaseToolset
from pydantic import Field

from pokedex_agent.agent_prompts import (
    build_root_agent_description,
    build_root_agent_instruction,
    build_root_agent_name,
    build_specialist_agent_description,
    build_specialist_agent_instruction,
    build_specialist_agent_name,
)
from pokedex_agent.model_config import get_live_model, get_model

type AgentTool = Callable[..., Mapping[str, object]] | BaseTool | BaseToolset


class PokedexAgent(LlmAgent):
    live_model: BaseLlm | str = Field(default_factory=get_live_model)

    @property
    def canonical_live_model(self) -> BaseLlm:
        if isinstance(self.live_model, BaseLlm):
            return self.live_model
        return LLMRegistry.new_llm(self.live_model)


def create_sub_agent(topic: str, tools: list[AgentTool]) -> Agent:
    return PokedexAgent(
        model=get_model(),
        live_model=get_live_model(),
        name=build_specialist_agent_name(topic),
        description=build_specialist_agent_description(topic),
        instruction=build_specialist_agent_instruction(topic),
        tools=tools,
    )


def create_root_agent(locale: str, sub_agents: list[Agent]) -> Agent:
    return PokedexAgent(
        model=get_model(),
        live_model=get_live_model(),
        name=build_root_agent_name(locale),
        description=build_root_agent_description(locale),
        instruction=build_root_agent_instruction(locale),
        sub_agents=sub_agents,
    )
