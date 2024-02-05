import os
import auction_art

bids = {}

print(auction_art.logo)

def clear_screen():
    """Function to clear screen before each output"""
    os.system('cls' if os.name == 'nt' else 'clear')

def add_bidder():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    more_bidders = input("Are there any more bidders? Type 'yes' or 'no'. ")

    bids[name] = bid

    if more_bidders == "yes":
        clear_screen()
        add_bidder()
    else:
        determine_winner()

def determine_winner():
    winning_bet = 0
    for name, bet in bids.items():
        if  bet > winning_bet:
            winning_bet = bet
            winner = name

    print(f"Congratulations {winner} you have won with a bid of ${winning_bet}")

add_bidder()
