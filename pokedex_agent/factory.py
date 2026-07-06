"""Shared helpers for building root and specialist agents."""

from google.adk.agents.llm_agent import Agent
from pokedex_agent.model_config import get_model
from pokedex_agent.tools.abilities import ability_tools
from pokedex_agent.tools.items import item_tools
from pokedex_agent.tools.meta import meta_tools
from pokedex_agent.tools.moves import move_tools
from pokedex_agent.tools.pokemon import pokemon_tools
from pokedex_agent.tools.world import world_tools


def create_sub_agent(
    name: str, description: str, instruction: str, tools: list
) -> Agent:
    return Agent(
        model=get_model(),
        name=name,
        description=description,
        instruction=instruction,
        tools=tools,
    )


def _build_agent(name: str, description: str, instruction: str) -> Agent:
    return Agent(
        model=get_model(),
        name=name,
        description=description,
        instruction=instruction,
        sub_agents=create_all_sub_agents(),
    )


def create_pokemon_agent() -> Agent:
    return create_sub_agent(
        name="pokemon_agent",
        description=(
            "Handles queries about Pokémon themselves: base stats, types, abilities, moves, "
            "species details, forms, colors, habitats, shapes, egg groups, natures, growth rates, "
            "genders, generations, characteristics, Pokédexes, and Pokéathlon stats."
        ),
        instruction=(
            "You are a Pokémon data specialist. "
            "Use the available tools to look up accurate data about Pokémon and return clear, "
            "well-formatted answers. "
            "Always use the tool — never guess stats or data from memory."
        ),
        tools=pokemon_tools,
    )


def create_move_agent() -> Agent:
    return create_sub_agent(
        name="move_agent",
        description=(
            "Handles queries about Pokémon moves and battle mechanics: move stats (power, accuracy, PP, type), "
            "TMs and HMs (machines), move ailments (status conditions), damage classes (physical/special/status), "
            "learn methods (level-up, egg, tutor), move targets, move categories, and battle styles."
        ),
        instruction=(
            "You are a Pokémon move and battle mechanics specialist. "
            "Use the available tools to look up accurate data about moves and return clear, "
            "well-formatted answers. "
            "Always use the tool — never guess move data from memory."
        ),
        tools=move_tools,
    )


def create_ability_agent() -> Agent:
    return create_sub_agent(
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


def create_item_agent() -> Agent:
    return create_sub_agent(
        name="item_agent",
        description=(
            "Handles queries about items and berries: item descriptions and effects, item categories "
            "and bag pockets, Fling effects, item attributes (holdable, consumable, etc.), "
            "berry growth data, berry flavors and nature preferences, and berry firmness categories."
        ),
        instruction=(
            "You are a Pokémon items and berries specialist. "
            "Use the available tools to look up accurate data about items and berries, "
            "and return clear, well-formatted answers. "
            "Always use the tool — never guess item or berry data from memory."
        ),
        tools=item_tools,
    )


def create_world_agent() -> Agent:
    return create_sub_agent(
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


def create_meta_agent() -> Agent:
    return create_sub_agent(
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


def create_all_sub_agents() -> list[Agent]:
    return [
        create_pokemon_agent(),
        create_move_agent(),
        create_ability_agent(),
        create_item_agent(),
        create_world_agent(),
        create_meta_agent(),
    ]
