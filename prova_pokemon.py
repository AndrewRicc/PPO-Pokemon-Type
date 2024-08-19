from pokemons.pokemonbattle import PokemonBattle
from pokemons.fetch import get_random_pokemon

user_pokemon = get_random_pokemon()
enemy_pokemon = get_random_pokemon()
PokemonBattle.choise_battle(user_pokemon, enemy_pokemon)