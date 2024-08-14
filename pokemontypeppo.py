import gym
import numpy as np
from pokemontype import PokemonType
from stable_baselines3 import PPO

# Definisci l'ambiente custom
class PokemonTypePPO(gym.Env):
    def __init__(self):
        super(PokemonTypePPO, self).__init__()

        # Definiamo un singolo spazio di osservazione discreto combinato
        self.observation_space = gym.spaces.Discrete((len(PokemonType) - 1) * len(PokemonType))  

        # Spazio d'azione: il tipo di Pokémon da scegliere
        self.action_space = gym.spaces.Discrete(len(PokemonType) - 1)  # Ignora il tipo NONE

    def reset(self):
        # Seleziona il primo tipo casualmente, escludendo NONE
        type1 = np.random.randint(1, len(PokemonType))

        # Seleziona il secondo tipo casualmente, che può essere NONE o diverso dal primo tipo
        while True:
            type2 = np.random.randint(0, len(PokemonType))
            if type2 != type1:  # Assicurati che il secondo tipo sia diverso dal primo
                break

        # Calcola l'indice combinato per lo spazio di osservazione
        self.state = (type1 - 1) * len(PokemonType) + type2
        return self.state

    def step(self, action):
        # Calcola la ricompensa basata sull'interazione dei tipi
        type1 = self.state // len(PokemonType) + 1
        type2 = self.state % len(PokemonType)

        defender_type1 = PokemonType(type1)
        defender_type2 = PokemonType(type2)
        attacker_type = PokemonType(action + 1)  # Compensa per ignorare NONE

        multiplier = PokemonType.interaction(defender_type1, defender_type2, attacker_type)

        if multiplier == 4:
            reward = 500
        elif multiplier == 2:
            reward = 50
        elif multiplier == 1:
            reward = 1
        elif multiplier == 0.5:
            reward = -10
        elif multiplier == 0.25:
            reward = -50
        elif multiplier == 0:
            reward = -500
        else:
            reward = 0

        # Definisce la fine dell'episodio, qui sempre True
        done = True

        # Nessuna informazione extra
        info = {}

        # Aggiorna lo stato

        return self.state, reward, done, info