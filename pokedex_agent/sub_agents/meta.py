"""Sub-agent for game metadata: versions, contests, languages, and evolution."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.meta import meta_tools


def create_meta_agent() -> Agent:
    return create_sub_agent(
        name="meta_agent",
        description=(
            "Handles game metadata queries: game versions and version groups, evolution chains and triggers, "
            "Pokémon Contest types and effects, Super Contest effects, and supported game languages."
        ),
        instruction=(
            "You are the Pokémon game-metadata specialist. "
            "Use the available tools to retrieve accurate version, evolution, contest, and language data "
            "and return clear, well-formatted answers. "
            "Always use tools for factual data instead of guessing from memory."
        ),
        tools=meta_tools,
    )


meta_agent = create_meta_agent()
