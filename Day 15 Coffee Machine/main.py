import os

# Data

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# functions


def ingredient_check(ingredients, resources):
    for ingredient, amount in ingredients.items():
        if amount > resources[ingredient]:
            print(f"Sorry not enough {ingredient}")
            return False
    return True


def make_drink(ingredients, resources):
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount


def pay(cost):
    paid = 0
    print(f"Your drink costs: ${cost}")
    paid += int(input("How Many Quarters?")) * 0.25
    paid += int(input("How Many Dimes?")) * 0.1
    paid += int(input("How Many Nickels?")) * 0.05
    paid += int(input("How Many Pennies?")) * 0.01
    return round(paid, 2)


def report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")


def clear():
    os.system('cls')


# Coffee Machine

def coffee_machine():

    request = input("What would you like? (espresso/cappuccino/latte) ")\
        .lower()

    if request in ['espresso', 'cappuccino', 'latte']:
        ingredients = MENU[request]['ingredients']
        cost = MENU[request]['cost']

        if ingredient_check(ingredients, resources):
            paid = pay(cost)
            if paid < cost:
                print(f"You've only inserted {paid}, transaction refunded.")
            elif paid > cost:
                make_drink(ingredients, resources)
                change = round(paid - cost, 2)
                print(f"Thank you. Here is your {request}.")
                print(f"Here is your change: ${change}")
            else:
                make_drink(ingredients, resources)
                print(f"Thank you. Here is your {request}.")

    elif request == 'report':
        report(resources)
    elif request == 'off':
        quit()

    coffee_machine()


coffee_machine()
