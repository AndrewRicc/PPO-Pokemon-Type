from pokemons.pokemontype import PokemonType


class PokemonMove():
    def __init__(
        self,
        name: str,
        type: PokemonType,
        base_p: int,
        accuracy: int,
        is_physic: bool
    ):
        if base_p == None:
            base_p = 0
        self.name = name
        self.type = type
        self.base_p = base_p
        self.accuracy = accuracy
        self.is_physic = is_physic

    
    def __str__(self) -> str:
        message = f"{self.name}:\n"
        message += f"\t- Type: {self.type.name}\n"
        message += f"\t- Base Power: {self.base_p}\n"
        message += f"\t- Accuracy: {self.accuracy}\n"
        
        return message