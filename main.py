import os
from arguments import get_args
from stable_baselines3 import PPO
from pokemontypeppo import PokemonTypePPO
from pokemontypeppotest import PokemonTypePPOTest
from stable_baselines3.common.env_util import make_vec_env

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
            model = PPO("MlpPolicy", env, n_epochs=4, verbose=1, device='cuda')
        model.learn(total_timesteps=args.total_timesteps, progress_bar=True)
        model.save(model_path)
        env.close()
        return
    elif args.mode == 'special_test':
        if args.type1 is None or args.type2 is None:
            print("Devi inserire i tipi per fare il test speciale")
            return
        
        if os.path.isfile(f"{model_path}.zip"):
            print(f"File del modello trovato: {model_path}. Caricamento del modello...")
            # Carica il modello esistente
            model = PPO.load(model_path, env)
        else:
            print("File del modello non trovato. Creazione di un nuovo modello...")
            # Crea un nuovo modello
            model = PPO("MlpPolicy", env, verbose=1)
        
        PokemonTypePPOTest.special_test(model, env, args.type1, args.type2)
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