#plan
# data is a list of dicts, so pick 2 random items from list and have A vs B
# "list[0][name], a list[0][desription] from list[0][country]"
# nicked a 

import random
from game_data import data
from art import logo, vs
import os

clear = lambda: os.system('cls')

print(logo)

def make_choice(data):
    return random.choice(data)

def format_choice(choice):
    name = choice['name']
    description = choice['description']
    country = choice['country']
    return f"{name}, a {description} from {country}."

def compare(a, b, guess):
    if a['follower_count'] > b['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'
 
def game():
    a = make_choice(data)
    b = make_choice(data)
    score = 0
    continue_game = True

    # swap b for a on subsequent goes

    while continue_game:
        a = b
        a = make_choice(data)

        while a == b:
            b = make_choice(data)

        print(f"Compare A: {format_choice(a)}")
        print(vs)
        print(f"Against B: {format_choice(b)}")

        guess = input("Who has more followers A or B? ").lower()

        clear()
        if compare(a, b, guess):
            score += 1
            print(f"Correct! Your current score is: {score}")
        else:
            print("Wrong! Game Over! Your final score is: {score}")
            continue_game = False

game()

# print(f"COMPARE A: {vs[0]['name']}, a {vs[0]['description']} from {vs[0]['country']}")
# print(vs)
# print(f"AGAINST B: {vs[1]['name']}, a {vs[1]['description']} from {vs[1]['country']}")

# # needs to check for valid input
# if input("Who has more followers A or B? ").to_upper() == 'A':
#     choice = 0
#     other = 1
# else:
#     other = 0
#     choice = 1

# # keep going until get one wrong, count score in the meantime.
# if vs[choice]['follower_count'] > vs[other]['follower_count']:
#     print("Correct")
# else:
#     print("Wrong")


