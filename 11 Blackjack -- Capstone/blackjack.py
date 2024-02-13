import random
import os
import blackjack_art


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
random_card = -1
player_score = -1
player_cards = []
dealer_cards = []
print(blackjack_art.logo)


def deal_card():
    random_card = random.choice(cards)
    return random_card


def determine_score(a):
    score = sum(a)
    if score > 21:
        if 11 in player_cards:
            score -= 10
            return score
        elif 11 not in player_cards:
            return score
    else:
        return score


def determine_winner():
    player_score = determine_score(player_cards)
    dealer_score = determine_score(dealer_cards)
    if player_score > 21:
        print(f"You Busted with a score of {player_score}")
    elif dealer_score > 21:
        print(f"You win the dealer busted with a score of {dealer_score}")
    elif player_score > dealer_score:
        print(
            f"You beat the dealer!!\nYou had a score of {player_score}\nThe dealer had a score of {dealer_score}"
        )
    else:
        print(
            f"The dealer beat you.\nYou had a score of {player_score}\nThe dealer had a score of {dealer_score}"
        )


def blackjack():
    player_cards.append(deal_card())
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())
    dealer_cards.append(deal_card())
    print(
        f"Your cards are {player_cards[0]} and {player_cards[1]} for a score of {determine_score(player_cards)}"
    )
    print(f"The dealer is showing {dealer_cards[0]}")

    did_hit = True

    while did_hit:
        if determine_score(dealer_cards) == 21:
            print("The dealer was dealt Blackjack\n You Loose!!")
            did_hit = False
            break
        elif determine_score(player_cards) == 21:
            print("BlackJack !!!")
            did_hit = False
            break
        hit = input("Would you like to get another card? 'y' or 'n' ")
        if hit == "y":
            player_cards.append(deal_card())
            print(
                f"Your new card is {player_cards[-1]} for a score of {determine_score(player_cards)}"
            )
            if determine_score(player_cards) > 21:
                determine_winner()
                did_hit = False
        else:
            while determine_score(dealer_cards) < 16:
                dealer_cards.append(deal_card())
            determine_winner()
            did_hit = False


def clear_screen():
    """Function to clear screen before each output"""
    os.system("cls" if os.name == "nt" else "clear")


blackjack()
while input("Would you like to play again? 'y' or 'n' ") == "y":
    clear_screen()
    player_cards = []
    dealer_cards = []
    blackjack()
