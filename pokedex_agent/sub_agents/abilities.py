from pokedex_agent.model_config import get_model
"""Sub-agent for Pokémon abilities and types."""

from google.adk.agents.llm_agent import Agent
from pokedex_agent.tools.abilities import ability_tools

ability_agent = Agent(
    model=get_model(),
    name="ability_agent",
    description=(
        "Handles queries about Pokémon abilities and types: ability descriptions and effects, "
        "which Pokémon have a given ability, type damage relations (strengths, weaknesses, immunities), "
        "and Pokémon belonging to a type."
    ),
    instruction=(
        "You are a Pokémon abilities and types specialist. "
        "Use the available tools to look up accurate data about abilities and types, "
        "and return clear, well-formatted answers. "
        "Always use the tool — never guess ability or type data from memory."
    ),
    tools=ability_tools,
)
