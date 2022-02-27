"""
This is the code for a coffe machine. The requeriments are:
- Prompt user by asking 'What would you like? (espresso/latte/cappuccino):'
- Turn off the Coffee Machine by entering 'off' to the prompt.
- Print report.
- Check resources sufficient?
- Process coins.
- Check transaction successful
- Make Coffee.
"""

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
    "money" : 0.0,
}


def payment_ok(price):
    """Check if the payment was ok and give change"""
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if total >= price:
        change = total - price
        quarters_change = int(change / 0.25)
        dimes_change = int((change - quarters_change * 0.25) / 0.1)
        nickles_change = int((change - quarters_change * 0.25 - dimes_change * 0.1) / 0.05)
        pennies_change = round((change - quarters_change * 0.25 - dimes_change * 0.1 - nickles_change * 0.05) / 0.01)
        print(f"Your change is {quarters_change} quarters, {dimes_change} dimes, {nickles_change} nickles, {pennies_change} pennies.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False


def check_resources(drink):
    """Check if the machine have enough resources and updates it"""
    global resources
    print(drink)
    if resources["water"] >= drink["ingredients"]["water"]:
        if resources["coffee"] >= drink["ingredients"]["coffee"]:
            if "milk" in drink["ingredients"].keys():
                if resources["milk"] >= drink["ingredients"]["milk"]:
                    return True
            else:
                return True
    else:
        if resources["water"] < drink["ingredients"]["water"]:
            print("Sorry, there is not enough water")
        if resources["milk"] < drink["ingredients"]["milk"]:
            print("Sorry, there is not enough milk")
        if resources["coffee"] < drink["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee")
        return False


def make_coffee(coffee):
    """Prepare coffee"""
    global resources
    resources["money"] += coffee["cost"]
    resources["water"] -= coffee["ingredients"]["water"]
    resources["coffee"] -= coffee["ingredients"]["coffee"]
    if "milk" in coffee["ingredients"].keys():
        resources["milk"] -= coffee["ingredients"]["milk"]


def print_report():
    """Print the current resources"""
    global resources
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


turn_off_machine: bool = False
while not turn_off_machine:
    user_order = input("What would you like? (espresso/latte/cappuccino)").lower()
    if user_order == "off":
        turn_off_machine = True
    elif user_order == "report":
        print_report()
    else:
        for beverage in MENU:
            if beverage == user_order:
                if check_resources(MENU[beverage]):
                    if payment_ok(MENU[beverage]["cost"]):
                        make_coffee(MENU[beverage])
                        print(f"Here is your {beverage}. Enjoy!")