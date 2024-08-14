from enum import Enum

class PokemonType(Enum):
    NONE        = 0
    NORMAL      = 1
    FIRE        = 2
    WATER       = 3
    GRASS       = 4
    ELECTRIC    = 5
    ICE         = 6
    FIGHTING    = 7
    POISON      = 8
    GROUND      = 9
    FLYING      = 10
    PSYCHIC     = 11
    BUG         = 12
    ROCK        = 13
    GHOST       = 14
    DRAGON      = 15
    DARK        = 16
    STEEL       = 17
    FAIRY       = 18

    @staticmethod
    def interaction(defender_type1, defender_type2, attacker_type):
        """Calcola il moltiplicatore dell'attacco basato sui tipi dei Pokémon."""
        # Definizione delle interazioni tra i tipi
        type_chart = {
            (PokemonType.NORMAL, PokemonType.ROCK): 0.5,
            (PokemonType.NORMAL, PokemonType.GHOST): 0.0,
            (PokemonType.NORMAL, PokemonType.STEEL): 0.5,
            (PokemonType.FIRE, PokemonType.FIRE): 0.5,
            (PokemonType.FIRE, PokemonType.WATER): 0.5,
            (PokemonType.FIRE, PokemonType.GRASS): 2.0,
            (PokemonType.FIRE, PokemonType.ICE): 2.0,
            (PokemonType.FIRE, PokemonType.BUG): 2.0,
            (PokemonType.FIRE, PokemonType.ROCK): 0.5,
            (PokemonType.FIRE, PokemonType.DRAGON): 0.5,
            (PokemonType.WATER, PokemonType.FIRE): 2.0,
            (PokemonType.WATER, PokemonType.WATER): 0.5,
            (PokemonType.WATER, PokemonType.GRASS): 0.5,
            (PokemonType.WATER, PokemonType.GROUND): 2.0,
            (PokemonType.WATER, PokemonType.ROCK): 2.0,
            (PokemonType.WATER, PokemonType.DRAGON): 0.5,
            (PokemonType.ELECTRIC, PokemonType.WATER): 2.0,
            (PokemonType.ELECTRIC, PokemonType.ELECTRIC): 0.5,
            (PokemonType.ELECTRIC, PokemonType.GRASS): 0.5,
            (PokemonType.ELECTRIC, PokemonType.GROUND): 0.0,
            (PokemonType.ELECTRIC, PokemonType.FLYING): 2.0,
            (PokemonType.ELECTRIC, PokemonType.DRAGON): 0.5,
            (PokemonType.GRASS, PokemonType.FIRE): 0.5,
            (PokemonType.GRASS, PokemonType.WATER): 2.0,
            (PokemonType.GRASS, PokemonType.GRASS): 0.5,
            (PokemonType.GRASS, PokemonType.POISON): 0.5,
            (PokemonType.GRASS, PokemonType.GROUND): 2.0,
            (PokemonType.GRASS, PokemonType.FLYING): 0.5,
            (PokemonType.GRASS, PokemonType.BUG): 0.5,
            (PokemonType.GRASS, PokemonType.ROCK): 2.0,
            (PokemonType.GRASS, PokemonType.DRAGON): 0.5,
            (PokemonType.GRASS, PokemonType.STEEL): 0.5,
            (PokemonType.ICE, PokemonType.FIRE): 0.5,
            (PokemonType.ICE, PokemonType.WATER): 0.5,
            (PokemonType.ICE, PokemonType.GRASS): 2.0,
            (PokemonType.ICE, PokemonType.ICE): 0.5,
            (PokemonType.ICE, PokemonType.GROUND): 2.0,
            (PokemonType.ICE, PokemonType.FLYING): 2.0,
            (PokemonType.ICE, PokemonType.DRAGON): 2.0,
            (PokemonType.ICE, PokemonType.STEEL): 0.5,
            (PokemonType.ICE, PokemonType.FAIRY): 1.0,
            (PokemonType.FIGHTING, PokemonType.NORMAL): 2.0,
            (PokemonType.FIGHTING, PokemonType.ICE): 2.0,
            (PokemonType.FIGHTING, PokemonType.POISON): 0.5,
            (PokemonType.FIGHTING, PokemonType.FLYING): 0.5,
            (PokemonType.FIGHTING, PokemonType.PSYCHIC): 0.5,
            (PokemonType.FIGHTING, PokemonType.BUG): 0.5,
            (PokemonType.FIGHTING, PokemonType.ROCK): 2.0,
            (PokemonType.FIGHTING, PokemonType.GHOST): 0.0,
            (PokemonType.FIGHTING, PokemonType.DARK): 2.0,
            (PokemonType.FIGHTING, PokemonType.STEEL): 2.0,
            (PokemonType.FIGHTING, PokemonType.FAIRY): 0.5,
            (PokemonType.POISON, PokemonType.GRASS): 2.0,
            (PokemonType.POISON, PokemonType.POISON): 0.5,
            (PokemonType.POISON, PokemonType.GROUND): 0.5,
            (PokemonType.POISON, PokemonType.ROCK): 0.5,
            (PokemonType.POISON, PokemonType.GHOST): 0.5,
            (PokemonType.POISON, PokemonType.STEEL): 0.0,
            (PokemonType.POISON, PokemonType.FAIRY): 2.0,
            (PokemonType.GROUND, PokemonType.FIRE): 2.0,
            (PokemonType.GROUND, PokemonType.ELECTRIC): 2.0,
            (PokemonType.GROUND, PokemonType.GRASS): 0.5,
            (PokemonType.GROUND, PokemonType.POISON): 2.0,
            (PokemonType.GROUND, PokemonType.FLYING): 0.0,
            (PokemonType.GROUND, PokemonType.BUG): 0.5,
            (PokemonType.GROUND, PokemonType.ROCK): 2.0,
            (PokemonType.GROUND, PokemonType.STEEL): 2.0,
            (PokemonType.FLYING, PokemonType.ELECTRIC): 0.5,
            (PokemonType.FLYING, PokemonType.GRASS): 2.0,
            (PokemonType.FLYING, PokemonType.FIGHTING): 2.0,
            (PokemonType.FLYING, PokemonType.BUG): 2.0,
            (PokemonType.FLYING, PokemonType.ROCK): 0.5,
            (PokemonType.FLYING, PokemonType.STEEL): 0.5,
            (PokemonType.PSYCHIC, PokemonType.FIGHTING): 2.0,
            (PokemonType.PSYCHIC, PokemonType.POISON): 2.0,
            (PokemonType.PSYCHIC, PokemonType.PSYCHIC): 0.5,
            (PokemonType.PSYCHIC, PokemonType.DARK): 0.0,
            (PokemonType.PSYCHIC, PokemonType.STEEL): 0.5,
            (PokemonType.BUG, PokemonType.FIRE): 0.5,
            (PokemonType.BUG, PokemonType.GRASS): 2.0,
            (PokemonType.BUG, PokemonType.FIGHTING): 0.5,
            (PokemonType.BUG, PokemonType.POISON): 0.5,
            (PokemonType.BUG, PokemonType.FLYING): 0.5,
            (PokemonType.BUG, PokemonType.PSYCHIC): 2.0,
            (PokemonType.BUG, PokemonType.GHOST): 0.5,
            (PokemonType.BUG, PokemonType.DARK): 2.0,
            (PokemonType.BUG, PokemonType.STEEL): 0.5,
            (PokemonType.BUG, PokemonType.FAIRY): 0.5,
            (PokemonType.ROCK, PokemonType.FIRE): 2.0,
            (PokemonType.ROCK, PokemonType.ICE): 2.0,
            (PokemonType.ROCK, PokemonType.FIGHTING): 0.5,
            (PokemonType.ROCK, PokemonType.GROUND): 0.5,
            (PokemonType.ROCK, PokemonType.FLYING): 2.0,
            (PokemonType.ROCK, PokemonType.BUG): 2.0,
            (PokemonType.ROCK, PokemonType.STEEL): 0.5,
            (PokemonType.GHOST, PokemonType.NORMAL): 0.0,
            (PokemonType.GHOST, PokemonType.PSYCHIC): 2.0,
            (PokemonType.GHOST, PokemonType.GHOST): 2.0,
            (PokemonType.GHOST, PokemonType.DARK): 0.5,
            (PokemonType.GHOST, PokemonType.FAIRY): 1.0,
            (PokemonType.DRAGON, PokemonType.DRAGON): 2.0,
            (PokemonType.DRAGON, PokemonType.STEEL): 0.5,
            (PokemonType.DRAGON, PokemonType.FAIRY): 0.0,
            (PokemonType.DARK, PokemonType.FIGHTING): 0.5,
            (PokemonType.DARK, PokemonType.PSYCHIC): 2.0,
            (PokemonType.DARK, PokemonType.GHOST): 2.0,
            (PokemonType.DARK, PokemonType.DARK): 0.5,
            (PokemonType.DARK, PokemonType.FAIRY): 0.5,
            (PokemonType.STEEL, PokemonType.FIRE): 0.5,
            (PokemonType.STEEL, PokemonType.WATER): 0.5,
            (PokemonType.STEEL, PokemonType.ELECTRIC): 0.5,
            (PokemonType.STEEL, PokemonType.ICE): 2.0,
            (PokemonType.STEEL, PokemonType.ROCK): 2.0,
            (PokemonType.STEEL, PokemonType.STEEL): 0.5,
            (PokemonType.STEEL, PokemonType.FAIRY): 2.0,
            (PokemonType.FAIRY, PokemonType.FIRE): 0.5,
            (PokemonType.FAIRY, PokemonType.FIGHTING): 2.0,
            (PokemonType.FAIRY, PokemonType.POISON): 0.5,
            (PokemonType.FAIRY, PokemonType.DRAGON): 2.0,
            (PokemonType.FAIRY, PokemonType.DARK): 2.0,
            (PokemonType.FAIRY, PokemonType.STEEL): 0.5,
        }
        
        # Se il secondo tipo difensivo è NONE, viene ignorato
        multiplier1 = type_chart.get((attacker_type, defender_type1), 1.0)
        multiplier2 = type_chart.get((attacker_type, defender_type2), 1.0)
        
        # Se il secondo tipo difensivo è NONE, il moltiplicatore è solo basato sul primo tipo
        if defender_type2 == PokemonType.NONE:
            return multiplier1
        
        return multiplier1 * multiplier2