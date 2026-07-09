"""Tools for Pokémon abilities and types."""

import pokebase as pb
from pokedex_agent.tools.utils import safe_fetch


@safe_fetch
def get_ability(ability_name: str) -> str:
    """Get information about a Pokémon ability (effect, Pokémon that have it).

    Args:
        ability_name: The ability name or its ID (e.g. 'overgrow' or '65').
    """
    return str(pb.ability(ability_name))


@safe_fetch
def get_type(type_name: str) -> str:
    """Get information about a Pokémon type (damage relations, Pokémon of this type).

    Args:
        type_name: The type name or its ID (e.g. 'fire', 'water', or '10').
    """
    return str(pb.type_(type_name))


ability_tools = [
    get_ability,
    get_type,
]
