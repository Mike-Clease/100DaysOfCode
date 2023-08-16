import random
from Rps_Pics import rock, paper, scissors

rps = ["rock", "paper", "scissors"]
pics = [rock, paper, scissors]

choice = input("Rock, paper or scissors? ").lower()

opponent = random.randint(0, 2)

[print(f"\n\nYou chose:\n{pics[i]}") for i, x in enumerate(rps) if x == choice]

print(f"\nYour opponent chose:\n{pics[opponent]}\n")

if rps[opponent] == choice:
    print(f"It's a draw")

elif (
    (rps[opponent] == "rock" and choice == "scissors")
    or (rps[opponent] == "scissors" and choice == "paper")
    or (rps[opponent] == "paper" and choice == "rock")
):
    print(f"You lose!")

else:
    print(f"You win!")
