import requests
import random
from pokemons.pokemon import Pokemon
from pokemons.pokemontype import PokemonType
from pokemons.pokemonmove import PokemonMove


def get_random_pokemon() -> Pokemon:
    return get_pokemon(random.sample(get_pokemons_name(), 1)[0])

def get_pokemons_name() -> str:
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')

    if response.status_code == 200:
        data: dict = response.json()
        ret = []
        for result in data['results']:
            ret.append(result['name'])
        return ret


def get_pokemon(name: str) -> Pokemon:
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')

    if response.status_code == 200:
        data: dict = response.json()

        moves: PokemonMove = []
        data['moves'] = random.sample(data['moves'], min(len(data['moves']), 4))

        for move in data['moves']:
            moves.append(get_move(move['move']['url']))

        tot_ev = 510
        ev_hp = ev_atk = ev_def = ev_atk_sp = ev_def_sp = ev_spe = 0

        while tot_ev > 0:
            # Incremento per HP
            increment = random.randint(0, min(252 - ev_hp, tot_ev))
            ev_hp += increment
            tot_ev -= increment

            # Incremento per Attack
            if tot_ev > 0:
                increment = random.randint(0, min(252 - ev_atk, tot_ev))
                ev_atk += increment
                tot_ev -= increment

            # Incremento per Defense
            if tot_ev > 0:
                increment = random.randint(0, min(252 - ev_def, tot_ev))
                ev_def += increment
                tot_ev -= increment

            # Incremento per Special Attack
            if tot_ev > 0:
                increment = random.randint(0, min(252 - ev_atk_sp, tot_ev))
                ev_atk_sp += increment
                tot_ev -= increment

            # Incremento per Special Defense
            if tot_ev > 0:
                increment = random.randint(0, min(252 - ev_def_sp, tot_ev))
                ev_def_sp += increment
                tot_ev -= increment

            # Incremento per Speed
            if tot_ev > 0:
                increment = random.randint(0, min(252 - ev_spe, tot_ev))
                ev_spe += increment
                tot_ev -= increment
        

        ret = Pokemon(
            name=data['species']['name'],
            weight=data['weight'],
            type1=PokemonType[data['types'][0]['type']['name'].upper()],
            type2=PokemonType[data['types'][1]['type']['name'].upper()] if len(data['types']) > 1 else PokemonType.NONE,
            nature='random',
            lvl=50,
            moves=moves,
            b_hp=data['stats'][0]['base_stat'],
            b_atk=data['stats'][1]['base_stat'],
            b_def=data['stats'][2]['base_stat'],
            b_atk_sp=data['stats'][3]['base_stat'],
            b_def_sp=data['stats'][4]['base_stat'],
            b_spe=data['stats'][5]['base_stat'],

            iv_hp=random.randint(0, 31),
            iv_atk=random.randint(0, 31),
            iv_def=random.randint(0, 31),
            iv_atk_sp=random.randint(0, 31),
            iv_def_sp=random.randint(0, 31),
            iv_spe=random.randint(0, 31),

            ev_hp=ev_hp,
            ev_atk=ev_atk,
            ev_def=ev_def,
            ev_atk_sp=ev_atk_sp,
            ev_def_sp=ev_def_sp,
            ev_spe=ev_spe
        )
        return ret
    
def get_move(url: str) -> PokemonMove:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        return PokemonMove(
            name=data['name'],
            type=PokemonType[data['type']['name'].upper()],
            base_p=data['power'],
            accuracy=data['accuracy'],
            is_physic=data['damage_class']['name'] == 'physical'
        )