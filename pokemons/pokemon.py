import math
import random
from typing import List, Union
from pokemons.basepokemon import BasePokemon
from pokemons.pokemonstatus import PokemonStatus
from pokemons.pokemontype import PokemonType
from pokemons.pokemonmove import PokemonMove


    
class Pokemon(BasePokemon):
    def __init__(
        self, 
        name: str, 
        weight: float, 
        type1: PokemonType, 
        type2: PokemonType = PokemonType.NONE, 
        nature: str = "hardy", 
        lvl: int = 1, 
        moves: List[PokemonMove] = [], 
        b_hp: int = 1, 
        b_atk: int = 1, 
        b_def: int = 1, 
        b_atk_sp: int = 1, 
        b_def_sp: int = 1, 
        b_spe: int = 1, 
        iv_hp: int = 0, 
        iv_atk: int = 0, 
        iv_def: int = 0, 
        iv_atk_sp: int = 0, 
        iv_def_sp: int = 0, 
        iv_spe: int = 0, 
        ev_hp: int = 0, 
        ev_atk: int = 0, 
        ev_def: int = 0, 
        ev_atk_sp: int = 0, 
        ev_def_sp: int = 0, 
        ev_spe: int = 0
    ):
        super().__init__(
            name=name, 
            weight=weight, 
            type1=type1, 
            type2=type2, 
            nature=nature, 
            lvl=lvl, 
            moves=moves, 
            b_hp=b_hp, 
            b_atk=b_atk, 
            b_def=b_def, 
            b_atk_sp=b_atk_sp, 
            b_def_sp=b_def_sp, 
            b_spe=b_spe, 
            iv_hp=iv_hp, 
            iv_atk=iv_atk, 
            iv_def=iv_def, 
            iv_atk_sp=iv_atk_sp, 
            iv_def_sp=iv_def_sp, 
            iv_spe=iv_spe, 
            ev_hp=ev_hp, 
            ev_atk=ev_atk, 
            ev_def=ev_def, 
            ev_atk_sp=ev_atk_sp, 
            ev_def_sp=ev_def_sp, 
            ev_spe=ev_spe
        )

    def attack_max_min(
        self,
        move_name_or_index: Union[str, int],
        defender: BasePokemon,
        is_raining: bool = False,
        is_sun: bool = False,
        is_tempeset: bool = False,
    ) -> tuple:
        move = None
        if isinstance(move_name_or_index, str):
            index = next((i for i, move in enumerate(self.moves) if move.name == move_name_or_index), None)
            if index is not None:
                move = self.moves[index]
            else:
                raise ValueError(f"Nessuna mossa con nome {move_name_or_index} è assegnata a questo Pokemon")
        elif isinstance(move_name_or_index, int):
            if move_name_or_index <= len(self.moves) and move_name_or_index > 0:
                move = self.moves[move_name_or_index - 1]
            else:
                raise ValueError("Index mossa non trovato")
        else:
            raise TypeError("Tipo non valido")
            
        rain_boost = is_raining and move.type == PokemonType.WATER
        rain_nerf = is_raining and move.type == PokemonType.FIRE
        rain_mult = 1.5 if rain_boost else 0.5 if rain_nerf else 1

        sun_boost = is_sun and move.type == PokemonType.FIRE
        sun_nerf = is_sun and move.type == PokemonType.WATER
        sun_mult = 1.5 if sun_boost else 0.5 if sun_nerf else 1

        stab = 1.5 if self.type1 == move.type or self.type2 == move.type else 1
        eff = PokemonType.interaction(defender.type1, defender.type2, move.type)
        roll = random.uniform(0.85, 1.00)
        # crit = 1.5 if random.randint(0, 999) < 417 else 1
        crit = 1
        burn_nerf = 0.5 if move.is_physic and self.status == PokemonStatus.BRN else 1

        atk = self.v_atk if move.is_physic else self.v_atk_sp
        defe = defender.v_def if move.is_physic else defender.v_def_sp

        max_mult = rain_mult * sun_mult * stab * eff * 1 * crit * burn_nerf
        min_mult = rain_mult * sun_mult * stab * eff * 0.85 * crit * burn_nerf
        max_dmg = math.floor((math.floor(((math.floor((2 * self.lvl) / 5) + 2) * move.base_p * math.floor(atk / defe)) / 50) + 2) * max_mult)
        min_dmg = math.floor((math.floor(((math.floor((2 * self.lvl) / 5) + 2) * move.base_p * math.floor(atk / defe)) / 50) + 2) * min_mult)
        
        
        return (max_dmg, min_dmg)
    
    def attack(
        self,
        move_name_or_index: Union[str, int],
        defender: BasePokemon,
        is_raining: bool = False,
        is_sun: bool = False,
        is_tempeset: bool = False,
    ) -> int:
        move = None
        if isinstance(move_name_or_index, str):
            index = next((i for i, move in enumerate(self.moves) if move.name == move_name_or_index), None)
            if index is not None:
                move = self.moves[index]
            else:
                raise ValueError(f"Nessuna mossa con nome {move_name_or_index} è assegnata a questo Pokemon")
        elif isinstance(move_name_or_index, int):
            if move_name_or_index <= len(self.moves) and move_name_or_index > 0:
                move = self.moves[move_name_or_index - 1]
            else:
                raise ValueError("Index mossa non trovato")
        else:
            raise TypeError("Tipo non valido")
            
        rain_boost = is_raining and move.type == PokemonType.WATER
        rain_nerf = is_raining and move.type == PokemonType.FIRE
        rain_mult = 1.5 if rain_boost else 0.5 if rain_nerf else 1

        sun_boost = is_sun and move.type == PokemonType.FIRE
        sun_nerf = is_sun and move.type == PokemonType.WATER
        sun_mult = 1.5 if sun_boost else 0.5 if sun_nerf else 1

        stab = 1.5 if self.type1 == move.type or self.type2 == move.type else 1
        eff = PokemonType.interaction(defender.type1, defender.type2, move.type)
        roll = random.uniform(0.85, 1.00)
        crit = 1.5 if random.randint(0, 999) < 417 else 1
        burn_nerf = 0.5 if move.is_physic and self.status == PokemonStatus.BRN else 1

        atk = self.v_atk if move.is_physic else self.v_atk_sp
        defe = defender.v_def if move.is_physic else defender.v_def_sp

        mult = rain_mult * sun_mult * stab * eff * roll * crit * burn_nerf
        print(f"{self.name} usa {move.name} su {defender.name}")
        if eff >= 2:
            print("E' superefficace")
        elif 0 < eff < 1:
            print("Non è molto efficace")
        return math.floor((math.floor(((math.floor((2 * self.lvl) / 5) + 2) * move.base_p * math.floor(atk / defe)) / 50) + 2) * mult)


    