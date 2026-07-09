"""Tools for Pokémon abilities and types."""

import pokebase as pb
from typing import NotRequired, TypedDict


class GetAbilityInput(TypedDict):
    ability_name: str


class GetAbilityOutput(TypedDict):
    value: str


class GetAbilityResponse(TypedDict):
    input: GetAbilityInput
    output: NotRequired[GetAbilityOutput]
    error: NotRequired[str]


class GetTypeInput(TypedDict):
    type_name: str


class GetTypeOutput(TypedDict):
    value: str


class GetTypeResponse(TypedDict):
    input: GetTypeInput
    output: NotRequired[GetTypeOutput]
    error: NotRequired[str]


def get_ability(ability_name: str) -> GetAbilityResponse:
    """Get information about a Pokémon ability (effect, Pokémon that have it).

    Args:
        ability_name: The ability name or its ID (e.g. 'overgrow' or '65').
    """
    return {
        "input": {"ability_name": ability_name},
        "output": {"value": str(pb.ability(ability_name))},
    }


def get_type(type_name: str) -> GetTypeResponse:
    """Get information about a Pokémon type (damage relations, Pokémon of this type).

    Args:
        type_name: The type name or its ID (e.g. 'fire', 'water', or '10').
    """
    return {
        "input": {"type_name": type_name},
        "output": {"value": str(pb.type_(type_name))},
    }


ability_tools = [
    get_ability,
    get_type,
]
