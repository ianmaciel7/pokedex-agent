"""Shared helpers for building root and specialist agents."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.model_config import get_model

IMAGE_RESPONSE_INSTRUCTION = (
    "When returning information about a specific Pokémon, item, berry, or other "
    "entity with an available visual equivalent, include one relevant image near "
    "the top of the answer using Markdown image syntax. Use tool-provided image "
    "URLs when available. Do not invent image URLs; if no relevant image is "
    "available, continue without one."
)


def create_sub_agent(
    name: str, description: str, instruction: str, tools: list
) -> Agent:
    return Agent(
        model=get_model(),
        name=name,
        description=description,
        instruction=f"{instruction} {IMAGE_RESPONSE_INSTRUCTION}",
        tools=tools,
    )


def create_root_agent(
    name: str, description: str, instruction: str, sub_agents: list[Agent]
) -> Agent:
    return Agent(
        model=get_model(),
        name=name,
        description=description,
        instruction=f"{instruction} {IMAGE_RESPONSE_INSTRUCTION}",
        sub_agents=sub_agents,
    )
