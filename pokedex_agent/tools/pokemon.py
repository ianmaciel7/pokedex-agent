"""Tools for core Pokémon data: species, stats, forms, natures, and related metadata."""

import pokebase as pb
from typing import NotRequired, TypedDict


class GetPokemonImageUrlInput(TypedDict):
    pokemon_name: str


class GetPokemonImageUrlOutput(TypedDict):
    url: str | None


class GetPokemonImageUrlResponse(TypedDict):
    input: GetPokemonImageUrlInput
    output: GetPokemonImageUrlOutput
    error: NotRequired[str]


class GetPokemonInput(TypedDict):
    pokemon_name: str


class GetPokemonOutput(TypedDict):
    value: str


class GetPokemonResponse(TypedDict):
    input: GetPokemonInput
    output: NotRequired[GetPokemonOutput]
    error: NotRequired[str]


class GetPokemonSpeciesInput(TypedDict):
    pokemon_species_name: str


class GetPokemonSpeciesOutput(TypedDict):
    value: str


class GetPokemonSpeciesResponse(TypedDict):
    input: GetPokemonSpeciesInput
    output: NotRequired[GetPokemonSpeciesOutput]
    error: NotRequired[str]


class GetPokemonColorInput(TypedDict):
    pokemon_color_name: str


class GetPokemonColorOutput(TypedDict):
    value: str


class GetPokemonColorResponse(TypedDict):
    input: GetPokemonColorInput
    output: NotRequired[GetPokemonColorOutput]
    error: NotRequired[str]


class GetPokemonFormInput(TypedDict):
    pokemon_form_name: str


class GetPokemonFormOutput(TypedDict):
    value: str


class GetPokemonFormResponse(TypedDict):
    input: GetPokemonFormInput
    output: NotRequired[GetPokemonFormOutput]
    error: NotRequired[str]


class GetPokemonHabitatInput(TypedDict):
    pokemon_habitat_name: str


class GetPokemonHabitatOutput(TypedDict):
    value: str


class GetPokemonHabitatResponse(TypedDict):
    input: GetPokemonHabitatInput
    output: NotRequired[GetPokemonHabitatOutput]
    error: NotRequired[str]


class GetPokemonShapeInput(TypedDict):
    pokemon_shape_name: str


class GetPokemonShapeOutput(TypedDict):
    value: str


class GetPokemonShapeResponse(TypedDict):
    input: GetPokemonShapeInput
    output: NotRequired[GetPokemonShapeOutput]
    error: NotRequired[str]


class GetCharacteristicInput(TypedDict):
    characteristic_id: str


class GetCharacteristicOutput(TypedDict):
    value: str


class GetCharacteristicResponse(TypedDict):
    input: GetCharacteristicInput
    output: NotRequired[GetCharacteristicOutput]
    error: NotRequired[str]


class GetGenderInput(TypedDict):
    gender_name: str


class GetGenderOutput(TypedDict):
    value: str


class GetGenderResponse(TypedDict):
    input: GetGenderInput
    output: NotRequired[GetGenderOutput]
    error: NotRequired[str]


class GetGenerationInput(TypedDict):
    generation_name: str


class GetGenerationOutput(TypedDict):
    value: str


class GetGenerationResponse(TypedDict):
    input: GetGenerationInput
    output: NotRequired[GetGenerationOutput]
    error: NotRequired[str]


class GetGrowthRateInput(TypedDict):
    growth_rate_name: str


class GetGrowthRateOutput(TypedDict):
    value: str


class GetGrowthRateResponse(TypedDict):
    input: GetGrowthRateInput
    output: NotRequired[GetGrowthRateOutput]
    error: NotRequired[str]


class GetNatureInput(TypedDict):
    nature_name: str


class GetNatureOutput(TypedDict):
    value: str


class GetNatureResponse(TypedDict):
    input: GetNatureInput
    output: NotRequired[GetNatureOutput]
    error: NotRequired[str]


class GetEggGroupInput(TypedDict):
    egg_group_name: str


class GetEggGroupOutput(TypedDict):
    value: str


class GetEggGroupResponse(TypedDict):
    input: GetEggGroupInput
    output: NotRequired[GetEggGroupOutput]
    error: NotRequired[str]


class GetStatInput(TypedDict):
    stat_name: str


class GetStatOutput(TypedDict):
    value: str


class GetStatResponse(TypedDict):
    input: GetStatInput
    output: NotRequired[GetStatOutput]
    error: NotRequired[str]


class GetPokeathlonStatInput(TypedDict):
    pokeathlon_stat_name: str


class GetPokeathlonStatOutput(TypedDict):
    value: str


class GetPokeathlonStatResponse(TypedDict):
    input: GetPokeathlonStatInput
    output: NotRequired[GetPokeathlonStatOutput]
    error: NotRequired[str]


class GetPokedexInput(TypedDict):
    pokedex_name: str


class GetPokedexOutput(TypedDict):
    value: str


class GetPokedexResponse(TypedDict):
    input: GetPokedexInput
    output: NotRequired[GetPokedexOutput]
    error: NotRequired[str]


def get_pokemon_image_url(pokemon_name: str) -> GetPokemonImageUrlResponse:
    """Get the official artwork image URL for a Pokémon.

    Args:
        pokemon_name: The name or Pokédex ID of the Pokémon (e.g. 'pikachu' or '25').
    """
    pokemon = pb.pokemon(pokemon_name)
    url = pokemon.sprites.other.official_artwork.front_default
    response: GetPokemonImageUrlResponse = {
        "input": {"pokemon_name": pokemon_name},
        "output": {"url": url},
    }
    if url is None:
        response["error"] = "No official artwork found."
    return response


def get_pokemon(pokemon_name: str) -> GetPokemonResponse:
    """Get base information about a Pokémon (stats, types, abilities, moves).

    Args:
        pokemon_name: The name or Pokédex ID of the Pokémon (e.g. 'pikachu' or '25').
    """
    return {
        "input": {"pokemon_name": pokemon_name},
        "output": {"value": str(pb.pokemon(pokemon_name))},
    }


def get_pokemon_species(pokemon_species_name: str) -> GetPokemonSpeciesResponse:
    """Get species-level information about a Pokémon (flavor text, evolution chain, egg groups).

    Args:
        pokemon_species_name: The name or ID of the Pokémon species.
    """
    return {
        "input": {"pokemon_species_name": pokemon_species_name},
        "output": {"value": str(pb.pokemon_species(pokemon_species_name))},
    }


def get_pokemon_color(pokemon_color_name: str) -> GetPokemonColorResponse:
    """Get Pokémon grouped by their color category.

    Args:
        pokemon_color_name: The color name (e.g. 'red', 'blue') or its ID.
    """
    return {
        "input": {"pokemon_color_name": pokemon_color_name},
        "output": {"value": str(pb.pokemon_color(pokemon_color_name))},
    }


def get_pokemon_form(pokemon_form_name: str) -> GetPokemonFormResponse:
    """Get information about a specific Pokémon form (e.g. Mega, Alolan).

    Args:
        pokemon_form_name: The name or ID of the Pokémon form.
    """
    return {
        "input": {"pokemon_form_name": pokemon_form_name},
        "output": {"value": str(pb.pokemon_form(pokemon_form_name))},
    }


def get_pokemon_habitat(pokemon_habitat_name: str) -> GetPokemonHabitatResponse:
    """Get Pokémon grouped by their habitat (e.g. 'cave', 'forest').

    Args:
        pokemon_habitat_name: The habitat name or its ID.
    """
    return {
        "input": {"pokemon_habitat_name": pokemon_habitat_name},
        "output": {"value": str(pb.pokemon_habitat(pokemon_habitat_name))},
    }


def get_pokemon_shape(pokemon_shape_name: str) -> GetPokemonShapeResponse:
    """Get Pokémon grouped by their body shape (e.g. 'quadruped', 'humanoid').

    Args:
        pokemon_shape_name: The shape name or its ID.
    """
    return {
        "input": {"pokemon_shape_name": pokemon_shape_name},
        "output": {"value": str(pb.pokemon_shape(pokemon_shape_name))},
    }


def get_characteristic(characteristic_id: str) -> GetCharacteristicResponse:
    """Get a Pokémon characteristic (highest stat flavour text, e.g. 'Loves to eat').

    Args:
        characteristic_id: The numeric ID of the characteristic.
    """
    return {
        "input": {"characteristic_id": characteristic_id},
        "output": {"value": str(pb.characteristic(characteristic_id))},
    }


def get_gender(gender_name: str) -> GetGenderResponse:
    """Get gender ratio and Pokémon lists for a gender category.

    Args:
        gender_name: The gender name ('male', 'female', or 'genderless') or its ID.
    """
    return {
        "input": {"gender_name": gender_name},
        "output": {"value": str(pb.gender(gender_name))},
    }


def get_generation(generation_name: str) -> GetGenerationResponse:
    """Get information about a game generation (e.g. 'generation-i').

    Args:
        generation_name: The generation name or its ID.
    """
    return {
        "input": {"generation_name": generation_name},
        "output": {"value": str(pb.generation(generation_name))},
    }


def get_growth_rate(growth_rate_name: str) -> GetGrowthRateResponse:
    """Get a Pokémon growth rate (experience curve, e.g. 'slow', 'fast').

    Args:
        growth_rate_name: The growth rate name or its ID.
    """
    return {
        "input": {"growth_rate_name": growth_rate_name},
        "output": {"value": str(pb.growth_rate(growth_rate_name))},
    }


def get_nature(nature_name: str) -> GetNatureResponse:
    """Get a Pokémon nature and the stats it raises/lowers (e.g. 'adamant').

    Args:
        nature_name: The nature name or its ID.
    """
    return {
        "input": {"nature_name": nature_name},
        "output": {"value": str(pb.nature(nature_name))},
    }


def get_egg_group(egg_group_name: str) -> GetEggGroupResponse:
    """Get a Pokémon egg group and its members (e.g. 'monster', 'fairy').

    Args:
        egg_group_name: The egg group name or its ID.
    """
    return {
        "input": {"egg_group_name": egg_group_name},
        "output": {"value": str(pb.egg_group(egg_group_name))},
    }


def get_stat(stat_name: str) -> GetStatResponse:
    """Get information about a base stat (e.g. 'speed', 'attack').

    Args:
        stat_name: The stat name or its ID.
    """
    return {
        "input": {"stat_name": stat_name},
        "output": {"value": str(pb.stat(stat_name))},
    }


def get_pokeathlon_stat(pokeathlon_stat_name: str) -> GetPokeathlonStatResponse:
    """Get information about a Pokéathlon stat (e.g. 'speed', 'power').

    Args:
        pokeathlon_stat_name: The Pokéathlon stat name or its ID.
    """
    return {
        "input": {"pokeathlon_stat_name": pokeathlon_stat_name},
        "output": {"value": str(pb.pokeathlon_stat(pokeathlon_stat_name))},
    }


def get_pokedex(pokedex_name: str) -> GetPokedexResponse:
    """Get information about a regional Pokédex (e.g. 'kanto', 'national').

    Args:
        pokedex_name: The Pokédex name or its ID.
    """
    return {
        "input": {"pokedex_name": pokedex_name},
        "output": {"value": str(pb.pokedex(pokedex_name))},
    }


pokemon_tools = [
    get_pokemon_image_url,
    get_pokemon,
    get_pokemon_species,
    get_pokemon_color,
    get_pokemon_form,
    get_pokemon_habitat,
    get_pokemon_shape,
    get_characteristic,
    get_gender,
    get_generation,
    get_growth_rate,
    get_nature,
    get_egg_group,
    get_stat,
    get_pokeathlon_stat,
    get_pokedex,
]
