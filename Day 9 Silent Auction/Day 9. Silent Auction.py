from clear import clear
from AuctionArt import logo

clear()
print(logo)

bids = {}
more_bids = True
# inputs
while more_bids:
    name = input("What is your name? ")
    bid = input("What is your bid? $")

    bids[name] = bid

    another = input("Are there anymore bids? Yes/No ")

    if another == 'No':
        more_bids = False
    
    clear()

max_bid = max(bids.values())
print(logo)
[print(f"The winner is {key} with a bid for ${value}") for key, value in bids.items() if value == max_bid]