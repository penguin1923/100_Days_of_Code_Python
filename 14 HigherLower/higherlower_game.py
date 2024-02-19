"""Higher Lower game using Instagram followers for day 14"""
import random
import os
import higherlower_data
import higherlower_art

def clear_screen():
    """Function to clear screen before each output"""
    os.system("cls" if os.name == "nt" else "clear")

def get_random_account():
    """returns a random account from the provided data"""
    return random.choice(higherlower_data.data)

def make_data_readable(random_letter):
    """formats the data randomly brought in to be something that is more readable"""
    rname = random_letter['name']
    rdescription = random_letter['description']
    rcountry=random_letter['country']
    return f"{rname}, {rdescription}, from {rcountry}"

def game_compare(guess, a_follower,b_follower):
    """figures out if the guess was correct, returns in TRUE/FALSE format"""
    if guess == "A" and a_follower>b_follower:
        return True
    elif guess == "B" and b_follower>a_follower:
        return True
    else:
        return False

def game():
    """main game section of higher/lower"""
    score = 0
    random_a = get_random_account()
    random_b = get_random_account()
    game_should_continue = True

    while game_should_continue:
        clear_screen()
        print(higherlower_art.logo)
        print(f"Your score is {score}")
        print("Compare A: "+make_data_readable(random_a))
        print(higherlower_art.vs)
        print("Against B: "+make_data_readable(random_b))
        guess=input("Who has more followers? Type 'A' or 'B': ").upper()

        game_should_continue = game_compare(guess,random_a['follower_count'],random_b['follower_count'])
        if game_should_continue is True:
            score += 1
            random_a = random_b
            random_b = get_random_account()
        else:
            clear_screen()
            print(higherlower_art.logo)
            print(f"You guessed incorrectly your score was {score}.")

game()

while input("Would you like to play again? 'y' or 'n' ") == "y":
    clear_screen()
    game()
