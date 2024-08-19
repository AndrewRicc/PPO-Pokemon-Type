import random
from pokemons.pokemon import Pokemon

class PokemonBattle():

    @staticmethod
    def choise_battle(user_pokemon: Pokemon, enemy_pokemon: Pokemon) -> None:
        done = False

        while not done:
            print(f"{user_pokemon.name} - You: {user_pokemon.hp} / {user_pokemon.max_hp} PS")
            print(f"{enemy_pokemon.name} - Enemy: {enemy_pokemon.hp} / {enemy_pokemon.max_hp} PS")
            print()
            print("1. Lotta")
            print("2. Stats")
            choise_input = input("Cosa vuoi fare? [1 - 2]: ")
            choise = 0
            try:
                choise = int(choise_input)
            except:
                print("Hai inserito un valore non valido, riprova")
                print()
                continue
            if choise == 1:
                print(f"1. {user_pokemon.moves[0].name} - {user_pokemon.moves[0].type.name}")
                print(f"2. {user_pokemon.moves[1].name} - {user_pokemon.moves[1].type.name}")
                print(f"3. {user_pokemon.moves[2].name} - {user_pokemon.moves[2].type.name}")
                print(f"4. {user_pokemon.moves[3].name} - {user_pokemon.moves[3].type.name}")
                print("5. Esci")
                fight_input = input("Cosa vuoi fare? [1 - 5]: ")
                fight_choise = 0
                try:
                    fight_choise = int(fight_input)
                except:
                    print("Hai inserito un valore non valido, riprova")
                    print()
                    continue
                
                if 0 < fight_choise < 5:
                    user_move_index = fight_choise
            elif choise == 2:
                print("Il tuo Pokemon: ")
                print(user_pokemon)
                print()
                print("Il Pokemon avversario: ")
                print(enemy_pokemon)
            else:
                print("Hai inserito un valore non valido, riprova")
                print()

            enemy_move_index = random.randint(1, 4)
            if choise == 1 and 0 < fight_choise < 5:
                if user_pokemon.spe > enemy_pokemon.spe:
                    enemy_pokemon.hp -= user_pokemon.attack(user_move_index, enemy_pokemon)
                    if enemy_pokemon.hp <= 0:
                        done = True
                        continue
                    user_pokemon.hp -= enemy_pokemon.attack(enemy_move_index, user_pokemon)
                    if user_pokemon.hp <= 0:
                        done = True
                        continue
                elif user_pokemon.spe < enemy_pokemon.spe:
                    user_pokemon.hp -= enemy_pokemon.attack(enemy_move_index, user_pokemon)
                    if user_pokemon.hp <= 0:
                        done = True
                        continue
                    enemy_pokemon.hp -= user_pokemon.attack(user_move_index, enemy_pokemon)
                    if enemy_pokemon.hp <= 0:
                        done = True
                        continue
                else:
                    tie = random.randint(1, 2)
                    if tie == 1:
                        enemy_pokemon.hp -= user_pokemon.attack(user_move_index, enemy_pokemon)
                        if enemy_pokemon.hp <= 0:
                            done = True
                            continue
                        user_pokemon.hp -= enemy_pokemon.attack(enemy_move_index, user_pokemon)
                        if user_pokemon.hp <= 0:
                            done = True
                            continue
                    else:
                        user_pokemon.hp -= enemy_pokemon.attack(enemy_move_index, user_pokemon)
                        if user_pokemon.hp <= 0:
                            done = True
                            continue
                        enemy_pokemon.hp -= user_pokemon.attack(user_move_index, enemy_pokemon)
                        if enemy_pokemon.hp <= 0:
                            done = True
                            continue
