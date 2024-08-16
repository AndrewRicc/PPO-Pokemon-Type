import math
from typing import List

from pokemon.pokemontype import PokemonType
from pokemon.pokemonmove import PokemonMove


class Pokemon():
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
        ev_spe: int = 0,
    ):
        all_natures = [
            'hardy', 
            'lonely', 
            'brave', 
            'adamant', 
            'naughty', 
            'bold', 
            'docile', 
            'relaxed', 
            'impish', 
            'lax', 
            'timid', 
            'hasty', 
            'serious', 
            'jolly', 
            'naive', 
            'modest', 
            'mild', 
            'quiet', 
            'bashful', 
            'rash', 
            'calm', 
            'gentle', 
            'sassy', 
            'careful', 
            'quirky'
        ]
        if lvl < 1:
            raise TypeError("Non puoi essere di livello inferiore a 1")
        if lvl > 100:
            raise TypeError("Non puoi essere di livello superiore a 100")
        if nature.lower() not in all_natures:
            raise TypeError("Non hai messo una natura valida")
        if type1 == PokemonType.NONE:
            raise TypeError("Il tipo principale non può essere NONE")
        if len(moves) > 4:
            raise TypeError("Non puoi inserire più di 4 mosse")
            
        if b_hp < 1: b_hp = 1
        if b_atk < 1: b_atk = 1
        if b_def < 1: b_def = 1
        if b_atk_sp < 1: b_atk_sp = 1
        if b_def_sp < 1: b_def_sp = 1
        if b_spe < 1: b_spe = 1
        
        if iv_hp < 0: iv_hp = 0
        if iv_atk < 0: iv_atk = 0
        if iv_def < 0: iv_def = 0
        if iv_atk_sp < 0: iv_atk_sp = 0
        if iv_def_sp < 0: iv_def_sp = 0
        if iv_spe < 0: iv_spe = 0
        
        if iv_hp > 31: iv_hp = 31
        if iv_atk > 31: iv_atk = 31
        if iv_def > 31: iv_def = 31
        if iv_atk_sp > 31: iv_atk_sp = 31
        if iv_def_sp > 31: iv_def_sp = 31
        if iv_spe > 31: iv_spe = 31

        if ev_hp < 0: ev_hp = 0
        if ev_atk < 0: ev_atk = 0
        if ev_def < 0: ev_def = 0
        if ev_atk_sp < 0: ev_atk_sp = 0
        if ev_def_sp < 0: ev_def_sp = 0
        if ev_spe < 0: ev_spe = 0

        if ev_hp > 252: ev_hp = 252
        if ev_atk > 252: ev_atk = 252
        if ev_def > 252: ev_def = 252
        if ev_atk_sp > 252: ev_atk_sp = 252
        if ev_def_sp > 252: ev_def_sp = 252
        if ev_spe > 252: ev_spe = 252

        if sum([ev_hp, ev_atk, ev_def, ev_atk_sp, ev_def_sp, ev_spe]) > 510:
            raise TypeError("Non puoi dare più di 510 EVs totali")
        
        self.name = name
        self.weight = weight
        
        self.lvl = lvl

        self.nature = nature.lower()
        self.type1 = type1
        self.type2 = type2
        self.moves = moves

        self.b_hp = b_hp
        self.b_atk = b_atk
        self.b_def = b_def
        self.b_atk_sp = b_atk_sp
        self.b_def_sp = b_def_sp
        self.b_spe = b_spe

        self.iv_hp = iv_hp
        self.iv_atk = iv_atk
        self.iv_def = iv_def
        self.iv_atk_sp = iv_atk_sp
        self.iv_def_sp = iv_def_sp
        self.iv_spe = iv_spe

        self.ev_hp = ev_hp
        self.ev_atk = ev_atk
        self.ev_def = ev_def
        self.ev_atk_sp = ev_atk_sp
        self.ev_def_sp = ev_def_sp
        self.ev_spe = ev_spe

        atk_boost = [all_natures[1], all_natures[2], all_natures[3], all_natures[4]]
        atk_nerf = [all_natures[5], all_natures[10], all_natures[15], all_natures[20]]

        def_boost = [all_natures[5], all_natures[7], all_natures[8], all_natures[9]]
        def_nerf = [all_natures[1], all_natures[11], all_natures[16], all_natures[21]]

        spe_boost = [all_natures[10], all_natures[11], all_natures[13], all_natures[14]]
        spe_nerf = [all_natures[2], all_natures[7], all_natures[17], all_natures[22]]

        atk_sp_boost = [all_natures[15], all_natures[16], all_natures[17], all_natures[19]]
        atk_sp_nerf = [all_natures[3], all_natures[8], all_natures[13], all_natures[23]]

        def_sp_boost = [all_natures[20], all_natures[21], all_natures[22], all_natures[23]]
        def_sp_nerf = [all_natures[4], all_natures[9], all_natures[14], all_natures[19]]

        self.atk_nature = 1.10 if self.nature in atk_boost else .90 if self.nature in atk_nerf else 1 
        self.def_nature = 1.10 if self.nature in def_boost else .90 if self.nature in def_nerf else 1 
        self.atk_sp_nature = 1.10 if self.nature in atk_sp_boost else .90 if self.nature in atk_sp_nerf else 1 
        self.def_sp_nature = 1.10 if self.nature in def_sp_boost else .90 if self.nature in def_sp_nerf else 1 
        self.spe_nature = 1.10 if self.nature in spe_boost else .90 if self.nature in spe_nerf else 1 

        self.max_hp = math.floor((((2 * self.b_hp + self.iv_hp + (self.ev_hp / 4)) * self.lvl) / 100) + self.lvl + 10)
        self.atk = math.floor(((((2 * self.b_hp + self.iv_hp + (self.ev_hp / 4)) * self.lvl) / 100) + 5) * self.atk_nature)
        self.defe = math.floor(((((2 * self.b_def + self.iv_def + (self.ev_def / 4)) * self.lvl) / 100) + 5) * self.def_nature)
        self.atk_sp = math.floor(((((2 * self.b_atk_sp + self.iv_atk_sp + (self.ev_atk_sp / 4)) * self.lvl) / 100) + 5) * self.atk_sp_nature)
        self.def_sp = math.floor(((((2 * self.b_def_sp + self.iv_def_sp + (self.ev_def_sp / 4)) * self.lvl) / 100) + 5) * self.def_sp_nature)
        self.spe = math.floor(((((2 * self.b_spe + self.iv_spe + (self.ev_spe / 4)) * self.lvl) / 100) + 5) * self.spe_nature)

        self.hp = self.max_hp

    def __str__(self) -> str:
        message = f"{self.name}:\n"
        message += f"\tLvl: {self.lvl}\n"
        message += f"\tNature: {self.nature.capitalize()}\n"
        message += f"\tType 1: {self.type1.name}\n"
        message += f"\tType 2: {self.type2.name}\n" if self.type2 is not PokemonType.NONE else ""
        message += f"\tHp: {self.max_hp}\n"
        message += f"\tAtk: {self.atk}\n"
        message += f"\tDef: {self.defe}\n"
        message += f"\tAtk_SP: {self.atk_sp}\n"
        message += f"\tDef_SP: {self.def_sp}\n"
        message += f"\tSpe: {self.spe}\n"
        message += f"\tMove 1: {self.moves[0]}\n" if len(self.moves) >= 1 else ""
        message += f"\tMove 2: {self.moves[1]}\n" if len(self.moves) >= 2 else ""
        message += f"\tMove 3: {self.moves[2]}\n" if len(self.moves) >= 3 else ""
        message += f"\tMove 4: {self.moves[3]}\n" if len(self.moves) >= 4 else ""

        return message
    
    