"""
Number Guessing Game Objectives:

Include an ASCII art logo.
Allow the player to submit a guess for a number between 1 and 100.
Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
If they got the answer correct, show the actual answer to the player.
Track the number of turns remaining.
If they run out of turns, provide feedback to the player. 
Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
"""
import random
import os
import guessing_art

def clear_screen():
    """Function to clear screen before each output"""
    os.system("cls" if os.name == "nt" else "clear")


print(guessing_art.logo)
print("Welcome to the Number Guessing Game!")

def game():
    """Guessing Game main function creates a random number between 1-100 then compares your guesses to it"""
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    easy_lives = 10
    hard_lives = 5
    guesses = 0
    if difficulty == 'easy':
        guesses = easy_lives
    else:
        guesses = hard_lives

    while guesses > 0:
        print(f"You have {guesses} attempts remaining to guess the number.")
        attempt = int(input("Make a guess: "))
        if attempt > random_number:
            print("Too High")
            guesses -= 1
        elif attempt < random_number:
            print("Too Low")
            guesses -=1
        elif attempt == random_number:
            print (f"You got it! The answer was {random_number}!")
            if guesses == 0:
                print("You ran out of lives. Better luck next time.")
            elif guesses == 2:
                print(f"You won with {guesses-1} attempt remaining. Great Job!")
            else:
                print(f"You won with {guesses-1} attempts remaining. Great Job!")
            guesses = -1

        if guesses >= 1:
            print("Guess Again")
        elif guesses == 0:
            print(f"You ran out of attempts. The correct answer was {random_number}")

game()

while input("Would you like to play again? 'y' or 'n' ") == "y":
    clear_screen()
    game()
