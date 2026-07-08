"""Sub-agent for game metadata: versions, contests, languages, and evolution."""

from google.adk.agents.llm_agent import Agent

from pokedex_agent.factory import create_sub_agent
from pokedex_agent.tools.meta import meta_tools


def create_meta_agent() -> Agent:
    return create_sub_agent(
        name="meta_agent",
        description=(
            "Handles queries about game metadata: game versions and version groups, "
            "evolution chains and evolution triggers, Pokémon Contest types and effects, "
            "Super Contest effects, and supported game languages."
        ),
        instruction=(
            "You are a Pokémon game metadata specialist. "
            "Use the available tools to look up accurate data about game versions, evolution, "
            "contests, and languages, and return clear, well-formatted answers. "
            "Always use the tool — never guess metadata from memory."
        ),
        tools=meta_tools,
    )


meta_agent = create_meta_agent()
