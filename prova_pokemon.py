from pokemon.pokemon import Pokemon
from pokemon.pokemonmove import PokemonMove
from pokemon.pokemontype import PokemonType

venusaur = Pokemon(
    name="Venusaur",
    weight=100.0,
    lvl=50,
    nature="Hardy",
    type1=PokemonType.GRASS,
    type2=PokemonType.POISON,
    moves=[
        PokemonMove(
            name="Fangobomba",
            type=PokemonType.POISON,
            base_p=90,
            accuracy=100,
            is_physic=False
        ),
        PokemonMove(
            name="Tossina",
            type=PokemonType.POISON,
            base_p=0,
            accuracy=100,
            is_physic=False
        ),
        PokemonMove(
            name="Parassiseme",
            type=PokemonType.GRASS,
            base_p=0,
            accuracy=100,
            is_physic=False
        ),
        PokemonMove(
            name="Protezione",
            type=PokemonType.NORMAL,
            base_p=0,
            accuracy=100,
            is_physic=False
        ),
    ],
    b_hp=80,
    b_atk=82,
    b_def=83,
    b_atk_sp=100,
    b_def_sp=100,
    b_spe=80,

    iv_hp=31,
    iv_atk=31,
    iv_def=31,
    iv_atk_sp=31,
    iv_def_sp=31,
    iv_spe=31,

    ev_hp=0,
    ev_atk=0,
    ev_def=0,
    ev_atk_sp=252,
    ev_def_sp=4,
    ev_spe=252
)

print(venusaur)