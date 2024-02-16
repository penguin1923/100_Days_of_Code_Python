import random
import os
import higherlower_data
import higherlower_art

def clear_screen():
    """Function to clear screen before each output"""
    os.system("cls" if os.name == "nt" else "clear")

def get_random_account():
    return random.choice(higherlower_data.data)

def make_data_readable():
    return

def game():
    clear_screen()
    print(higherlower_art.logo)
    score = 0
    random_a = get_random_account()
    random_b = get_random_account()
    game_should_continue = True

    while game_should_continue:
        print("Hello")
    # need to format random_a before printing
        print(random_a["name"])

        game_should_continue = False



game()