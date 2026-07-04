"""Sub-agent for game meta-data: versions, contests, languages, and evolution."""

from google.adk.agents.llm_agent import Agent
from pokedex_agent.tools.meta import meta_tools

meta_agent = Agent(
    model="gemini-2.0-flash",
    name="meta_agent",
    description=(
        "Handles queries about game meta-data: game versions and version groups, "
        "evolution chains and evolution triggers, Pokémon Contest types and effects, "
        "Super Contest effects, and supported game languages."
    ),
    instruction=(
        "You are a Pokémon game meta-data specialist. "
        "Use the available tools to look up accurate data about game versions, evolution, "
        "contests, and languages, and return clear, well-formatted answers. "
        "Always use the tool — never guess meta-data from memory."
    ),
    tools=meta_tools,
)
