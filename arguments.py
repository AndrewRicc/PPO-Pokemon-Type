"""
	This file contains the arguments to parse at command line.
	File main.py will call get_args, which then the arguments
	will be returned.
"""
import argparse

def get_args():
	"""
		Description:
		Parses arguments at command line.

		Parameters:
			None

		Return:
			args - the arguments parsed
	"""
	parser = argparse.ArgumentParser()

	parser.add_argument('--mode', dest='mode', type=str, default='train')                       # can be 'train' or 'test'
	parser.add_argument('--model_path', dest='model_path', type=str, default='ppo_pokemon_type')
	parser.add_argument('--timesteps', dest='total_timesteps', type=int, default='500_000')

	args = parser.parse_args()

	return args
