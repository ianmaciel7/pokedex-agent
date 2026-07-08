"""Sub-agent package exports."""

from .abilities import ability_agent, create_ability_agent
from .items import create_item_agent, item_agent
from .meta import create_meta_agent, meta_agent
from .moves import create_move_agent, move_agent
from .pokemon import create_pokemon_agent, pokemon_agent
from .world import create_world_agent, world_agent


def create_all_sub_agents():
    return [
        create_pokemon_agent(),
        create_move_agent(),
        create_ability_agent(),
        create_item_agent(),
        create_world_agent(),
        create_meta_agent(),
    ]


all_sub_agents = [
    pokemon_agent,
    move_agent,
    ability_agent,
    item_agent,
    world_agent,
    meta_agent,
]

__all__ = [
    "pokemon_agent",
    "move_agent",
    "ability_agent",
    "item_agent",
    "world_agent",
    "meta_agent",
    "create_pokemon_agent",
    "create_move_agent",
    "create_ability_agent",
    "create_item_agent",
    "create_world_agent",
    "create_meta_agent",
    "create_all_sub_agents",
    "all_sub_agents",
]
