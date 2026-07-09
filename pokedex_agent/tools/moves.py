"""Tools for Pokémon moves and battle mechanics."""

import pokebase as pb
from typing import NotRequired, TypedDict


class GetMoveInput(TypedDict):
    move_name: str


class GetMoveOutput(TypedDict):
    value: str


class GetMoveResponse(TypedDict):
    input: GetMoveInput
    output: NotRequired[GetMoveOutput]
    error: NotRequired[str]


class GetMoveAilmentInput(TypedDict):
    move_ailment_name: str


class GetMoveAilmentOutput(TypedDict):
    value: str


class GetMoveAilmentResponse(TypedDict):
    input: GetMoveAilmentInput
    output: NotRequired[GetMoveAilmentOutput]
    error: NotRequired[str]


class GetMoveBattleStyleInput(TypedDict):
    move_battle_style_name: str


class GetMoveBattleStyleOutput(TypedDict):
    value: str


class GetMoveBattleStyleResponse(TypedDict):
    input: GetMoveBattleStyleInput
    output: NotRequired[GetMoveBattleStyleOutput]
    error: NotRequired[str]


class GetMoveCategoryInput(TypedDict):
    move_category_name: str


class GetMoveCategoryOutput(TypedDict):
    value: str


class GetMoveCategoryResponse(TypedDict):
    input: GetMoveCategoryInput
    output: NotRequired[GetMoveCategoryOutput]
    error: NotRequired[str]


class GetMoveDamageClassInput(TypedDict):
    move_damage_class_name: str


class GetMoveDamageClassOutput(TypedDict):
    value: str


class GetMoveDamageClassResponse(TypedDict):
    input: GetMoveDamageClassInput
    output: NotRequired[GetMoveDamageClassOutput]
    error: NotRequired[str]


class GetMoveLearnMethodInput(TypedDict):
    move_learn_method_name: str


class GetMoveLearnMethodOutput(TypedDict):
    value: str


class GetMoveLearnMethodResponse(TypedDict):
    input: GetMoveLearnMethodInput
    output: NotRequired[GetMoveLearnMethodOutput]
    error: NotRequired[str]


class GetMoveTargetInput(TypedDict):
    move_target_name: str


class GetMoveTargetOutput(TypedDict):
    value: str


class GetMoveTargetResponse(TypedDict):
    input: GetMoveTargetInput
    output: NotRequired[GetMoveTargetOutput]
    error: NotRequired[str]


class GetMachineInput(TypedDict):
    machine_id: str


class GetMachineOutput(TypedDict):
    value: str


class GetMachineResponse(TypedDict):
    input: GetMachineInput
    output: NotRequired[GetMachineOutput]
    error: NotRequired[str]


def get_move(move_name: str) -> GetMoveResponse:
    """Get detailed information about a Pokémon move (power, accuracy, type, PP).

    Args:
        move_name: The move name or its ID (e.g. 'flamethrower' or '53').
    """
    return {
        "input": {"move_name": move_name},
        "output": {"value": str(pb.move(move_name))},
    }


def get_move_ailment(move_ailment_name: str) -> GetMoveAilmentResponse:
    """Get a move ailment (status condition a move can inflict, e.g. 'burn', 'paralysis').

    Args:
        move_ailment_name: The ailment name or its ID.
    """
    return {
        "input": {"move_ailment_name": move_ailment_name},
        "output": {"value": str(pb.move_ailment(move_ailment_name))},
    }


def get_move_battle_style(
    move_battle_style_name: str,
) -> GetMoveBattleStyleResponse:
    """Get a move battle style used in Pokémon Battle Palace (e.g. 'attack', 'defense').

    Args:
        move_battle_style_name: The battle style name or its ID.
    """
    return {
        "input": {"move_battle_style_name": move_battle_style_name},
        "output": {"value": str(pb.move_battle_style(move_battle_style_name))},
    }


def get_move_category(move_category_name: str) -> GetMoveCategoryResponse:
    """Get a move category (e.g. 'damage', 'ailment', 'heal').

    Args:
        move_category_name: The category name or its ID.
    """
    return {
        "input": {"move_category_name": move_category_name},
        "output": {"value": str(pb.move_category(move_category_name))},
    }


def get_move_damage_class(
    move_damage_class_name: str,
) -> GetMoveDamageClassResponse:
    """Get a move damage class (e.g. 'physical', 'special', 'status').

    Args:
        move_damage_class_name: The damage class name or its ID.
    """
    return {
        "input": {"move_damage_class_name": move_damage_class_name},
        "output": {"value": str(pb.move_damage_class(move_damage_class_name))},
    }


def get_move_learn_method(
    move_learn_method_name: str,
) -> GetMoveLearnMethodResponse:
    """Get a method by which a Pokémon can learn a move (e.g. 'level-up', 'egg', 'tutor').

    Args:
        move_learn_method_name: The learn method name or its ID.
    """
    return {
        "input": {"move_learn_method_name": move_learn_method_name},
        "output": {"value": str(pb.move_learn_method(move_learn_method_name))},
    }


def get_move_target(move_target_name: str) -> GetMoveTargetResponse:
    """Get a move target (who the move affects, e.g. 'selected-pokemon', 'all-opponents').

    Args:
        move_target_name: The target name or its ID.
    """
    return {
        "input": {"move_target_name": move_target_name},
        "output": {"value": str(pb.move_target(move_target_name))},
    }


def get_machine(machine_id: str) -> GetMachineResponse:
    """Get information about a TM or HM machine (which move it teaches, which games it appears in).

    Args:
        machine_id: The numeric ID of the machine.
    """
    return {
        "input": {"machine_id": machine_id},
        "output": {"value": str(pb.machine(machine_id))},
    }


move_tools = [
    get_move,
    get_move_ailment,
    get_move_battle_style,
    get_move_category,
    get_move_damage_class,
    get_move_learn_method,
    get_move_target,
    get_machine,
]
