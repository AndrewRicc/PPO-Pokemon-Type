# Pokemon Type PPO
This repo is used to train an AI predicting which type of Pokemon move should be used against a Pokemon
## Installation
- Install [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)
- Use `python -m venv venv` to create a virtual enviroment
- Use `./venv/Scripts/Activate.ps1` on Windows | Use `./venv/bin/activate` on Unix 
- Use `pip install -r requirements.txt` to install all requisites
- Run `python main.py`
- Optional arguments:
    - `--mode=train` for training mode. Default value = train
    - `--mode=test` for test mode. Default value = train
    - `--timesteps` to set total_timesteps. Default value = 500000
    - `--model_path` to set starting base model. Default value = ppo_pokemon_type
