"""
This is the first project usins OOP. It's the code for the day before (coffee machine) but using OOP
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink_menu = Menu()
coffee_machine = CoffeeMaker()
payments = MoneyMachine()
turn_off = False

while not turn_off:
    order = input(f"What would you like to order? ({drink_menu.get_items()})")
    if order == "off":
        turn_off = True
    elif order == "report":
        coffee_machine.report()
        payments.report()
    elif order in drink_menu.get_items():
        if coffee_machine.is_resource_sufficient( drink_menu.find_drink( order ) ) and payments.make_payment(drink_menu.find_drink(order).cost):
            coffee_machine.make_coffee(drink_menu.find_drink(order))