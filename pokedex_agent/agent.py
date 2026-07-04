"""Root orchestrator agent — delegates to specialized sub-agents by context."""

from google.adk.agents.llm_agent import Agent
from pokedex_agent.sub_agents import all_sub_agents

root_agent = Agent(
    model="gemini-2.0-flash",
    name="root_agent",
    description="An orchestrator that answers any question about Pokémon by routing to the right specialist.",
    instruction=(
        "You are the Pokémon Assistant orchestrator. "
        "When a user asks a question, identify its topic and delegate to the correct specialist sub-agent:\n\n"
        "• pokemon_agent  — Pokémon stats, species, forms, natures, egg groups, Pokédexes, etc.\n"
        "• move_agent     — Moves, TMs/HMs, damage classes, learn methods, battle styles.\n"
        "• ability_agent  — Abilities and type matchups / damage relations.\n"
        "• item_agent     — Items, Poké Balls, berries and their flavors.\n"
        "• world_agent    — Locations, encounter rates, regions, Pal Park.\n"
        "• meta_agent     — Game versions, evolution chains/triggers, Contests, languages.\n\n"
        "Always delegate — never answer from memory alone. "
        "If a question spans multiple topics, call the most relevant sub-agent first, "
        "then follow up with additional sub-agents if needed."
    ),
    sub_agents=all_sub_agents,
)
