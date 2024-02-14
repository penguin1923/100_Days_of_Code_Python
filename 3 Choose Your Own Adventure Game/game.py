print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input("You come to the end of a hallway and can either go 'left' or 'right'. Pick one now.\n")
if choice.lower() == "left":
    choice = input("You now are at a river. Should you 'swim' or 'wait' for the boat?\n")
    if choice.lower() == "wait":
        choice = input("Now you are in front of three doors and you need to pick one before the pirates on the beach catch you. Should you go in the 'red' on the 'blue' one or the 'yellow' one?\n")
        if choice.lower() == "yellow":
            print("You Win!!! The room is full of treasure and there is an uber waiting outside to carry it all home.")
        elif choice.lower() == "blue":
            print("You immediately regret this decision as a million fire ants attack you cleaning you all the way to the bone")
        elif choice.lower() == "red":
            print("The door was heavy as you pushed it open. Unfortunately due to its weight you were unable to close it before the pirates saw you and captured you.")
        else:
            print("Game Over")
    elif choice.lower() == "swim":
        print("This was a terrible choice as the undertow dragged you down never to be seen again.")
    else:
        print("Game Over")
elif choice.lower() == "right":
    print("Right was not right!! You walked to the end of the next hallway to find out that you have been trapped in a never-ending maze")
else:
    print("Game Over")
    