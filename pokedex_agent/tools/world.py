"""Tools for locations, encounters, and regions."""

import pokebase as pb
from typing import NotRequired, TypedDict


class GetLocationInput(TypedDict):
    location_name: str


class GetLocationOutput(TypedDict):
    value: str


class GetLocationResponse(TypedDict):
    input: GetLocationInput
    output: NotRequired[GetLocationOutput]
    error: NotRequired[str]


class GetLocationAreaInput(TypedDict):
    location_area_name: str


class GetLocationAreaOutput(TypedDict):
    value: str


class GetLocationAreaResponse(TypedDict):
    input: GetLocationAreaInput
    output: NotRequired[GetLocationAreaOutput]
    error: NotRequired[str]


class GetRegionInput(TypedDict):
    region_name: str


class GetRegionOutput(TypedDict):
    value: str


class GetRegionResponse(TypedDict):
    input: GetRegionInput
    output: NotRequired[GetRegionOutput]
    error: NotRequired[str]


class GetEncounterConditionInput(TypedDict):
    encounter_condition_name: str


class GetEncounterConditionOutput(TypedDict):
    value: str


class GetEncounterConditionResponse(TypedDict):
    input: GetEncounterConditionInput
    output: NotRequired[GetEncounterConditionOutput]
    error: NotRequired[str]


class GetEncounterConditionValueInput(TypedDict):
    encounter_condition_value_name: str


class GetEncounterConditionValueOutput(TypedDict):
    value: str


class GetEncounterConditionValueResponse(TypedDict):
    input: GetEncounterConditionValueInput
    output: NotRequired[GetEncounterConditionValueOutput]
    error: NotRequired[str]


class GetEncounterMethodInput(TypedDict):
    encounter_method_name: str


class GetEncounterMethodOutput(TypedDict):
    value: str


class GetEncounterMethodResponse(TypedDict):
    input: GetEncounterMethodInput
    output: NotRequired[GetEncounterMethodOutput]
    error: NotRequired[str]


class GetPalParkAreaInput(TypedDict):
    pal_park_area_name: str


class GetPalParkAreaOutput(TypedDict):
    value: str


class GetPalParkAreaResponse(TypedDict):
    input: GetPalParkAreaInput
    output: NotRequired[GetPalParkAreaOutput]
    error: NotRequired[str]


def get_location(location_name: str) -> GetLocationResponse:
    """Get information about a location in the Pokémon world (e.g. 'pallet-town').

    Args:
        location_name: The location name or its ID.
    """
    return {
        "input": {"location_name": location_name},
        "output": {"value": str(pb.location(location_name))},
    }


def get_location_area(location_area_name: str) -> GetLocationAreaResponse:
    """Get a specific area within a location and its wild Pokémon encounter rates.

    Args:
        location_area_name: The location area name or its ID.
    """
    return {
        "input": {"location_area_name": location_area_name},
        "output": {"value": str(pb.location_area(location_area_name))},
    }


def get_region(region_name: str) -> GetRegionResponse:
    """Get information about a game region (e.g. 'kanto', 'johto').

    Args:
        region_name: The region name or its ID.
    """
    return {
        "input": {"region_name": region_name},
        "output": {"value": str(pb.region(region_name))},
    }


def get_encounter_condition(
    encounter_condition_name: str,
) -> GetEncounterConditionResponse:
    """Get a condition that affects wild Pokémon encounters (e.g. 'swarm', 'time').

    Args:
        encounter_condition_name: The condition name or its ID.
    """
    return {
        "input": {"encounter_condition_name": encounter_condition_name},
        "output": {"value": str(pb.encounter_condition(encounter_condition_name))},
    }


def get_encounter_condition_value(
    encounter_condition_value_name: str,
) -> GetEncounterConditionValueResponse:
    """Get a specific value for an encounter condition (e.g. 'time-morning').

    Args:
        encounter_condition_value_name: The condition value name or its ID.
    """
    return {
        "input": {"encounter_condition_value_name": encounter_condition_value_name},
        "output": {
            "value": str(pb.encounter_condition_value(encounter_condition_value_name))
        },
    }


def get_encounter_method(encounter_method_name: str) -> GetEncounterMethodResponse:
    """Get a method of encountering wild Pokémon (e.g. 'walk', 'surf', 'fishing').

    Args:
        encounter_method_name: The encounter method name or its ID.
    """
    return {
        "input": {"encounter_method_name": encounter_method_name},
        "output": {"value": str(pb.encounter_method(encounter_method_name))},
    }


def get_pal_park_area(pal_park_area_name: str) -> GetPalParkAreaResponse:
    """Get a Pal Park area (e.g. 'field', 'forest', 'mountain', 'pond', 'sea').

    Args:
        pal_park_area_name: The Pal Park area name or its ID.
    """
    return {
        "input": {"pal_park_area_name": pal_park_area_name},
        "output": {"value": str(pb.pal_park_area(pal_park_area_name))},
    }


world_tools = [
    get_location,
    get_location_area,
    get_region,
    get_encounter_condition,
    get_encounter_condition_value,
    get_encounter_method,
    get_pal_park_area,
]
