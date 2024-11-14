from operator import truediv

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 18
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 18
        },
        "cost": 3.5,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(ordered_ingredients):
    """Returns true if order can be made, and false if ingredients are insufficient"""
    for item in ordered_ingredients:
        if ordered_ingredients[item]>=resources[item]:
            print(f"sorry, we are out of {item}")
            return  False
    return True


def process_coins():
    """Returns total calculated amount from coins inserted."""
    print("Please, insert coins.")
    total = int(input("How many quarters?:"))*0.25
    total += int(input("How many dimes?:"))*0.1
    total += int(input("How many nickels?:"))*0.05
    total += int(input("How many pennies?:"))*0.01
    return total

def is_transaction_success(amount_received, drink_cost):
    """Returns True if payment is successful, False if payment isn't sufficient."""
    if amount_received>drink_cost:
        change = round(amount_received-drink_cost, 2)
        print(f"Here's ${change} in change.")
        global profit
        profit+=drink_cost

        return True
    else:
        print("sorry, payment is insufficient. Amount refunded")
        return False

def make_coffee(chosed_drink, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -=drink_ingredients[item]
    print(f"Hey! enjoy your {chosed_drink}☕")

is_on = True
while is_on:
    choice = input('What do you want to order, espresso, latte,or cappuccino: ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}")
        print(f"money:${profit}")
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
           payment =  process_coins()
           if is_transaction_success(payment, drink['cost']):
               make_coffee(choice, drink["ingredients"])

