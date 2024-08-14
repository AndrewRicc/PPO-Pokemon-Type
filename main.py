import os
from arguments import get_args
from stable_baselines3 import PPO
from pokemontypeppo import PokemonTypePPO
from pokemontypeppotest import PokemonTypePPOTest

def main(args):
    model_path = args.model_path
    env = PokemonTypePPO()
    
    if args.mode == 'train':
        if os.path.isfile(f"{model_path}.zip"):
            print(f"File del modello trovato: {model_path}. Caricamento del modello...")
            # Carica il modello esistente
            model = PPO.load(model_path, env)
        else:
            print("File del modello non trovato. Creazione di un nuovo modello...")
            # Crea un nuovo modello
            model = PPO("MlpPolicy", env, verbose=1)
        model.learn(total_timesteps=args.total_timesteps)
        model.save(model_path)
        env.close()
        return
    else:
        if os.path.isfile(f"{model_path}.zip"):
            print(f"File del modello trovato: {model_path}. Caricamento del modello...")
            # Carica il modello esistente
            model = PPO.load(model_path, env)
        else:
            print("File del modello non trovato. Creazione di un nuovo modello...")
            # Crea un nuovo modello
            model = PPO("MlpPolicy", env, verbose=1)

        PokemonTypePPOTest.test(model, env)


if __name__ == '__main__':
	args = get_args()
	main(args)