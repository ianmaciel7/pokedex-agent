"""Sub-agent for locations, encounters, and regions."""

from google.adk.agents.llm_agent import Agent
from pokedex_agent.tools.world import world_tools

world_agent = Agent(
    model="gemini-2.0-flash",
    name="world_agent",
    description=(
        "Handles queries about the Pokémon world: locations and their sub-areas, "
        "wild Pokémon encounter rates per area, encounter methods (walking, surfing, fishing), "
        "encounter conditions and their values (time of day, weather, swarms), "
        "game regions (Kanto, Johto, etc.), and Pal Park areas."
    ),
    instruction=(
        "You are a Pokémon world and encounters specialist. "
        "Use the available tools to look up accurate data about locations and encounters, "
        "and return clear, well-formatted answers. "
        "Always use the tool — never guess location or encounter data from memory."
    ),
    tools=world_tools,
)
