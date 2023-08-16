from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What do you want? {menu.get_items()} ").lower()

    if choice in ['espresso', 'latte', 'cappuccino']:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        is_on = False
