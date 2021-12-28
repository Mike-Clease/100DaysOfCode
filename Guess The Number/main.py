#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from clear import clear
import random

def game():
    clear()
    print(logo)

    number = random.randint(1, 100)
    win = False
    turns = select_mode()

    while turns > 0 and not win:
        turns, win = compare_guess(number, turns, win)

    if turns == 0 and not win:
        print("Sorry. You lose.")

    if input("Would you like to play again? y/n ") == 'y':
            game()

def select_mode():
    mode = input("Chose your difficulty setting: easy / hard ").lower()

    if mode == 'easy':
        turns = 10
        return turns
    elif mode == 'hard':
        turns = 5
        return turns
    else:
        print("You didn't enter a valid mode, try again.")
        select_mode()

def compare_guess(number, turns, win):
    guess = int(input(f"You have {turns} remaining. Guess a number: "))

    if guess == number:
        print(f"Correct! I was thinking of {number}")
        win = True
    elif guess > number:
        print("Too high.")
        print("Guess again")
        turns -= 1
    elif guess < number:
        print("Too low.")
        print("Guess again")
        turns -= 1

    return turns, win

game()
