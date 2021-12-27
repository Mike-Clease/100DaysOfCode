############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# draw hand of 2 cards to player and pc
# check value of hands
# if hand > 21 that player loses
# else gets a choice
# aces count as 11 unless hand > 21 then it's a 1
# 1st cards are revealed
# computer draws until hand > 16

import random
from clear import clear
from art import logo

def draw(list):
    """
    Adds a random card to a specified hand.
    If that card is an ace and that would put the hand over 21
    then it counts as a 1 rather than an 11.
    """
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck)
    # if an ace is drawn and that would put the list over 21 then the ace counts as a 1
    new_hand = list.copy()
    new_hand.append(card)

    if sum(new_hand) > 21 and card == 11:
        card = 1

    return list.append(card)

def show_hand(hand):
    print(f"Your hand is: {hand}. Total score: {sum(hand)}")



def blackjack():
    clear()
    print(logo)

    player = []
    dealer = []

    draw(player)
    draw(player)
    show_hand(player)

    draw(dealer)
    draw(dealer)
    print(f"The dealer has: [{dealer[0]}, ?]")

    another = True

    while another and sum(player) <= 21:
        if input("Would you like to draw another card? y/n ") == 'n':
            another = False
        else:
            clear()
            draw(player)
            show_hand(player)
            print(f"The dealer has: [{dealer[0]}, ?]")

    while sum(dealer) < 16:
        draw(dealer)

    # Print final scores
    clear()
    print(f"Your final hand: {player}. Final score: {sum(player)}.")
    print(f"Dealers final hand: {dealer}. Final score: {sum(dealer)}")

    # Print result message - this is a little over complex, also why not just sum earlier rather than repeat it...
    if sum(player) == 21 and (sum(dealer) < 21 or sum(dealer) > 21):
        print("Blackjack! You win!")
    elif sum(player) == 21 and sum(dealer) == 21:
        print("The dealer scores Blackjack! You lose.")
    elif (sum(player) < 21 or sum(player) > 21) and sum(dealer) == 21:
        print("The dealer scores Blackjack! You lose.")
    elif sum(player) > 21:
        print("you lose")
    elif sum(dealer) > 21:
        print("you win")
    elif sum(player) > sum(dealer):
        print("You win!")
    elif sum(dealer) > sum(player):
        print("You lose!")

    if input("Would you like to play again? y/n ") == 'y':
        blackjack()
    else:
        print("Goodbye!")

clear()
blackjack()