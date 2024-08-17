
from pokemons.pokemontype import PokemonType
from stable_baselines3 import PPO
from pokemontypeppo import PokemonTypePPO

class PokemonTypePPOTest():
    def __init__(self):
        super(PokemonTypePPOTest, self).__init__()

    @staticmethod
    def test(model: PPO, env: PokemonTypePPO):

        # Test del modello
        for _ in range(10):  # Esegui 10 test
            obs = env.reset()
            done = False
            while not done:
                action, _states = model.predict(obs, deterministic=True)
                
                type1 = (obs // len(PokemonType)) + 1
                type2 = obs % len(PokemonType)

                # Converti l'osservazione e l'azione in tipi di Pokémon
                defender_type1, defender_type2 = PokemonType(type1), PokemonType(type2)
                attacker_type = PokemonType(action + 1)  # +1 perché l'azione 0 corrisponde al tipo 1
                
                print(f"Osservazione: Difensore - Tipo 1: {defender_type1.name}, Tipo 2: {defender_type2.name}")
                print(f"Azione: Attaccante - Tipo: {attacker_type.name}")
                
                obs, reward, done, info = env.step(action)
                print(f"Ricompensa: {reward}\n")

    @staticmethod
    def special_test(model: PPO, env: PokemonTypePPO, type1: int, type2: int):
        
        obs = (type1 - 1) * len(PokemonType) + type2
        env.state = obs

        action, _states = model.predict(obs)

        defender_type1, defender_type2 = PokemonType(type1), PokemonType(type2)
        attacker_type = PokemonType(action + 1)
        
        
        print(f"Osservazione: Difensore - Tipo 1: {defender_type1.name}, Tipo 2: {defender_type2.name}")
        print(f"Azione: Attaccante - Tipo: {attacker_type.name}")
        
        obs, reward, done, info = env.step(action)
        print(f"Ricompensa: {reward}\n")