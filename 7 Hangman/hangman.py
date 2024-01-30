"""Hangman Game"""
import random
import os
import hangman_words
import hangman_art


chosen_word = random.choice(hangman_words.word_list)
display = []
lives = 6
blank = "_"
for letter in range(len(chosen_word)):
    display.append(blank)
print(hangman_art.logo)
## print(f'Pssst, the solution is {chosen_word}.')
print(f"{' '.join(display)}")
end_of_game = False

def clear_screen():
    """Function to clear screen before each output"""
    os.system('cls' if os.name == 'nt' else 'clear')

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear_screen()
    count=-1
    if guess in display:
        print("You already guessed "+ guess + " please guess again\n")
        print(f"{' '.join(display)}")
        print(hangman_art.stages[lives])
        continue
    for letter in chosen_word:
        count += 1
        if letter == guess:
            display[count]=letter
    if guess not in chosen_word:
        print(guess +" is not in the current word.\n")
        lives -=1
    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])

    if blank not in display:
        end_of_game = True
        print("You Win!!")
    elif lives == 0:
        end_of_game = True
        print("You Loose!!")
