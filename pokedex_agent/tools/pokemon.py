"""Tools for core Pokémon data: species, stats, forms, natures, and related metadata."""

import pokebase as pb


def get_pokemon_image_url(pokemon_name: str) -> str:
    """Get the official artwork image URL for a Pokémon.

    Args:
        pokemon_name: The name or Pokédex ID of the Pokémon (e.g. 'pikachu' or '25').
    """
    pokemon = pb.pokemon(pokemon_name)
    pokemon_id = pokemon.id
    return (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/"
        f"sprites/pokemon/other/official-artwork/{pokemon_id}.png"
    )


def get_pokemon(pokemon_name: str) -> str:
    """Get base information about a Pokémon (stats, types, abilities, moves).

    Args:
        pokemon_name: The name or Pokédex ID of the Pokémon (e.g. 'pikachu' or '25').
    """
    return str(pb.pokemon(pokemon_name))


def get_pokemon_species(pokemon_species_name: str) -> str:
    """Get species-level information about a Pokémon (flavor text, evolution chain, egg groups).

    Args:
        pokemon_species_name: The name or ID of the Pokémon species.
    """
    return str(pb.pokemon_species(pokemon_species_name))


def get_pokemon_color(pokemon_color_name: str) -> str:
    """Get Pokémon grouped by their color category.

    Args:
        pokemon_color_name: The color name (e.g. 'red', 'blue') or its ID.
    """
    return str(pb.pokemon_color(pokemon_color_name))


def get_pokemon_form(pokemon_form_name: str) -> str:
    """Get information about a specific Pokémon form (e.g. Mega, Alolan).

    Args:
        pokemon_form_name: The name or ID of the Pokémon form.
    """
    return str(pb.pokemon_form(pokemon_form_name))


def get_pokemon_habitat(pokemon_habitat_name: str) -> str:
    """Get Pokémon grouped by their habitat (e.g. 'cave', 'forest').

    Args:
        pokemon_habitat_name: The habitat name or its ID.
    """
    return str(pb.pokemon_habitat(pokemon_habitat_name))


def get_pokemon_shape(pokemon_shape_name: str) -> str:
    """Get Pokémon grouped by their body shape (e.g. 'quadruped', 'humanoid').

    Args:
        pokemon_shape_name: The shape name or its ID.
    """
    return str(pb.pokemon_shape(pokemon_shape_name))


def get_characteristic(characteristic_id: str) -> str:
    """Get a Pokémon characteristic (highest stat flavour text, e.g. 'Loves to eat').

    Args:
        characteristic_id: The numeric ID of the characteristic.
    """
    return str(pb.characteristic(characteristic_id))


def get_gender(gender_name: str) -> str:
    """Get gender ratio and Pokémon lists for a gender category.

    Args:
        gender_name: The gender name ('male', 'female', or 'genderless') or its ID.
    """
    return str(pb.gender(gender_name))


def get_generation(generation_name: str) -> str:
    """Get information about a game generation (e.g. 'generation-i').

    Args:
        generation_name: The generation name or its ID.
    """
    return str(pb.generation(generation_name))


def get_growth_rate(growth_rate_name: str) -> str:
    """Get a Pokémon growth rate (experience curve, e.g. 'slow', 'fast').

    Args:
        growth_rate_name: The growth rate name or its ID.
    """
    return str(pb.growth_rate(growth_rate_name))


def get_nature(nature_name: str) -> str:
    """Get a Pokémon nature and the stats it raises/lowers (e.g. 'adamant').

    Args:
        nature_name: The nature name or its ID.
    """
    return str(pb.nature(nature_name))


def get_egg_group(egg_group_name: str) -> str:
    """Get a Pokémon egg group and its members (e.g. 'monster', 'fairy').

    Args:
        egg_group_name: The egg group name or its ID.
    """
    return str(pb.egg_group(egg_group_name))


def get_stat(stat_name: str) -> str:
    """Get information about a base stat (e.g. 'speed', 'attack').

    Args:
        stat_name: The stat name or its ID.
    """
    return str(pb.stat(stat_name))


def get_pokeathlon_stat(pokeathlon_stat_name: str) -> str:
    """Get information about a Pokéathlon stat (e.g. 'speed', 'power').

    Args:
        pokeathlon_stat_name: The Pokéathlon stat name or its ID.
    """
    return str(pb.pokeathlon_stat(pokeathlon_stat_name))


def get_pokedex(pokedex_name: str) -> str:
    """Get information about a regional Pokédex (e.g. 'kanto', 'national').

    Args:
        pokedex_name: The Pokédex name or its ID.
    """
    return str(pb.pokedex(pokedex_name))


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
