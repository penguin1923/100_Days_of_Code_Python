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

def game_compare(guess, a_follower,b_follower):
    
    if guess == "A" and a_follower>b_follower:
        return True
    elif guess == "B" and b_follower>a_follower:
        return True
    else:
        return False

def game():
    clear_screen()
    print(higherlower_art.logo)
    score = 0
    random_a = get_random_account()
    a_format=f"{random_a['name']}, {random_a['description']}, from {random_a['country']}"
    random_b = get_random_account()
    b_format=f"{random_b['name']}, {random_b['description']}, from {random_b['country']}"
    game_should_continue = True

    while game_should_continue:
    # need to format random_a before printing
        print("Compare A: "+a_format)
        print(higherlower_art.vs)
        print("Against B: "+b_format)
        guess=input("Who has more followers? Type 'A' or 'B'").upper()

        game_should_continue = False
        game_should_continue = game_compare(guess,random_a['follower_count'],random_b['follower_count'])
        while game_should_continue:
            score+=
            random_a = random_b
            random_b = get_random_account()



game()