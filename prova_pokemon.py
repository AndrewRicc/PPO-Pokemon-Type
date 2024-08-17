from pokemons.fetch import get_random_pokemon

'''venusaur = Pokemon(
    name="Venusaur",
    weight=100.0,
    type1=PokemonType.GRASS,
    type2=PokemonType.POISON,
    nature="Timid",
    lvl=50,
    moves=[
        PokemonMove(
            name="Fangobomba",
            type=PokemonType.POISON,
            base_p=90,
            accuracy=100,
            is_physic=False
        ),
        PokemonMove(
            name="Geoforza",
            type=PokemonType.GROUND,
            base_p=90,
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
    ev_def=4,
    ev_atk_sp=252,
    ev_def_sp=0,
    ev_spe=252
)
#nihilego = Pokemon(
    name='Nihilego',
    weight=1,
    type1=PokemonType.ROCK,
    type2=PokemonType.POISON,
    nature='Timid',
    lvl=50,
    moves=[],
    b_hp=109,
    b_atk=53,
    b_def=47,
    b_atk_sp=127,
    b_def_sp=131,
    b_spe=103,

    iv_hp=31,
    iv_atk=31,
    iv_def=31,
    iv_atk_sp=31,
    iv_def_sp=31,
    iv_spe=31,

    ev_hp=0,
    ev_atk=0,
    ev_def=80,
    ev_atk_sp=176,
    ev_def_sp=0,
    ev_spe=252
)'''

# max_dmg, min_dmg = venusaur.attack('Geoforza', nihilego)

# print(f"{min_dmg} - {max_dmg} PS inflitti")


print('Pokemon generato: \n')
print(get_random_pokemon())