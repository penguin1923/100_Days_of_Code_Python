"""added random to play the computer in this game"""
import random

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

picture = [ROCK,PAPER,SCISSORS]
player_choice=int(input("What do you choose? '0' for Rock, '1' for Paper or '2' for Scissors. \n"))
computer_choice=random.randint(0,2)
try:
    print("You Chose:")
    print(picture[player_choice])
    print("Computer chose:")
    print(picture[computer_choice])
except:
    pass

if player_choice > 2 or player_choice < 0:
    print("Thats not a valid option you lose")
elif player_choice == computer_choice:
    print("Its a tie")
elif player_choice > computer_choice:
    if player_choice == 2 and computer_choice == 1:
        print("You Win scissors beats paper!!")
    elif player_choice == 2 and computer_choice == 0:
        print("You Lose rock beats scissors")
    else:
        print("You win Paper beats rock")
else:
    if computer_choice == 2 and player_choice == 1:
        print("You Lose scissors beats paper!!")
    elif computer_choice == 2 and player_choice == 0:
        print("You Win rock beats scissors")
    else:
        print("You Lose Paper beats rock")
