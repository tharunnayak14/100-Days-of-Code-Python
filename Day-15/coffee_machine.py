MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
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
# order = input("What would you like? (espresso/latte/cappuccino):")
# print(MENU[order]['ingredients'])

# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”


# TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.

continue_coffee = True


# TODO: 3. Print report.

def print_report():
    for key in resources:
        print(f"{key}: {resources[key]}")


# TODO: 4. Check resources sufficient?

def check_resources():
    for key in resources:
        if MENU[order]["ingredients"][key] > resources[key]:
            print(f"Sorry there is not enough {key}")
            return False

    return True


# availability = check_resources()
# print(availability)

# TODO: 5. Process coins

def process_coins():
    if check_resources():
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))

        total_amount = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        return total_amount


# TODO: 6. Check transaction successful?

def deduct_resources():
    for key in resources:
        resources[key] = resources[key] - MENU[order]['ingredients'][key]


def check_transaction():
    total_amount = process_coins()
    if total_amount >= MENU[order]['cost']:
        change = total_amount - MENU[order]['cost']
        print(f"Here is {round(change, 2)} dollars in change")
        # TODO: 7. Make Coffee.
        deduct_resources()
        print_report()
        print(f"Here is your {order}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


while continue_coffee:
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == 'off':
        continue_coffee = False
    elif order == 'report':
        print_report()
    else:
        check_transaction()


