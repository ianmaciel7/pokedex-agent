"""Tools for game metadata: versions, contests, languages, and evolution."""

import pokebase as pb
from typing import NotRequired, TypedDict


class GetVersionInput(TypedDict):
    version_name: str


class GetVersionOutput(TypedDict):
    value: str


class GetVersionResponse(TypedDict):
    input: GetVersionInput
    output: NotRequired[GetVersionOutput]
    error: NotRequired[str]


class GetVersionGroupInput(TypedDict):
    version_group_name: str


class GetVersionGroupOutput(TypedDict):
    value: str


class GetVersionGroupResponse(TypedDict):
    input: GetVersionGroupInput
    output: NotRequired[GetVersionGroupOutput]
    error: NotRequired[str]


class GetEvolutionChainInput(TypedDict):
    evolution_chain_id: str


class GetEvolutionChainOutput(TypedDict):
    value: str


class GetEvolutionChainResponse(TypedDict):
    input: GetEvolutionChainInput
    output: NotRequired[GetEvolutionChainOutput]
    error: NotRequired[str]


class GetEvolutionTriggerInput(TypedDict):
    evolution_trigger_name: str


class GetEvolutionTriggerOutput(TypedDict):
    value: str


class GetEvolutionTriggerResponse(TypedDict):
    input: GetEvolutionTriggerInput
    output: NotRequired[GetEvolutionTriggerOutput]
    error: NotRequired[str]


class GetContestTypeInput(TypedDict):
    contest_type_name: str


class GetContestTypeOutput(TypedDict):
    value: str


class GetContestTypeResponse(TypedDict):
    input: GetContestTypeInput
    output: NotRequired[GetContestTypeOutput]
    error: NotRequired[str]


class GetContestEffectInput(TypedDict):
    contest_effect_id: str


class GetContestEffectOutput(TypedDict):
    value: str


class GetContestEffectResponse(TypedDict):
    input: GetContestEffectInput
    output: NotRequired[GetContestEffectOutput]
    error: NotRequired[str]


class GetSuperContestEffectInput(TypedDict):
    super_contest_effect_id: str


class GetSuperContestEffectOutput(TypedDict):
    value: str


class GetSuperContestEffectResponse(TypedDict):
    input: GetSuperContestEffectInput
    output: NotRequired[GetSuperContestEffectOutput]
    error: NotRequired[str]


class GetLanguageInput(TypedDict):
    language_name: str


class GetLanguageOutput(TypedDict):
    value: str


class GetLanguageResponse(TypedDict):
    input: GetLanguageInput
    output: NotRequired[GetLanguageOutput]
    error: NotRequired[str]


def get_version(version_name: str) -> GetVersionResponse:
    """Get information about a specific game version (e.g. 'red', 'gold', 'sword').

    Args:
        version_name: The game version name or its ID.
    """
    return {
        "input": {"version_name": version_name},
        "output": {"value": str(pb.version(version_name))},
    }


def get_version_group(version_group_name: str) -> GetVersionGroupResponse:
    """Get a version group (paired games sharing mechanics, e.g. 'red-blue', 'sun-moon').

    Args:
        version_group_name: The version group name or its ID.
    """
    return {
        "input": {"version_group_name": version_group_name},
        "output": {"value": str(pb.version_group(version_group_name))},
    }


def get_evolution_chain(evolution_chain_id: str) -> GetEvolutionChainResponse:
    """Get the full evolution chain for a Pokémon family by chain ID.

    Args:
        evolution_chain_id: The numeric ID of the evolution chain.
    """
    return {
        "input": {"evolution_chain_id": evolution_chain_id},
        "output": {"value": str(pb.evolution_chain(evolution_chain_id))},
    }


def get_evolution_trigger(evolution_trigger_name: str) -> GetEvolutionTriggerResponse:
    """Get an evolution trigger (the condition that triggers evolution, e.g. 'level-up', 'trade').

    Args:
        evolution_trigger_name: The evolution trigger name or its ID.
    """
    return {
        "input": {"evolution_trigger_name": evolution_trigger_name},
        "output": {"value": str(pb.evolution_trigger(evolution_trigger_name))},
    }


def get_contest_type(contest_type_name: str) -> GetContestTypeResponse:
    """Get a Pokémon Contest type (e.g. 'cool', 'cute', 'smart').

    Args:
        contest_type_name: The contest type name or its ID.
    """
    return {
        "input": {"contest_type_name": contest_type_name},
        "output": {"value": str(pb.contest_type(contest_type_name))},
    }


def get_contest_effect(contest_effect_id: str) -> GetContestEffectResponse:
    """Get the effect of a move when used in a Pokémon Contest.

    Args:
        contest_effect_id: The numeric ID of the contest effect.
    """
    return {
        "input": {"contest_effect_id": contest_effect_id},
        "output": {"value": str(pb.contest_effect(contest_effect_id))},
    }


def get_super_contest_effect(
    super_contest_effect_id: str,
) -> GetSuperContestEffectResponse:
    """Get the effect of a move when used in a Super Contest.

    Args:
        super_contest_effect_id: The numeric ID of the super contest effect.
    """
    return {
        "input": {"super_contest_effect_id": super_contest_effect_id},
        "output": {"value": str(pb.super_contest_effect(super_contest_effect_id))},
    }


def get_language(language_name: str) -> GetLanguageResponse:
    """Get information about a supported game language (e.g. 'en', 'ja', 'fr').

    Args:
        language_name: The language name or its ID.
    """
    return {
        "input": {"language_name": language_name},
        "output": {"value": str(pb.language(language_name))},
    }


meta_tools = [
    get_version,
    get_version_group,
    get_evolution_chain,
    get_evolution_trigger,
    get_contest_type,
    get_contest_effect,
    get_super_contest_effect,
    get_language,
]
