#plan
# data is a list of dicts, so pick 2 random items from list and have A vs B
# "list[0][name], a list[0][desription] from list[0][country]"

import random
from game_data import data
from art import logo, vs

print(logo)

a, b = random.choices(data, k=2)

print(f"{a['name']}, a {a['description']} from {a['country']}")
print(vs)
print(f"{b['name']}, a {b['description']} from {b['country']}")