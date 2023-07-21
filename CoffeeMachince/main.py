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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def sufficient_ingredients(coffee_type):
    for item in coffee_type:
        if coffee_type[item] > resources[item]:
            print(f"sorry there is not enough {item}")
            return False
        else:
            return True
def coins_count():
    print("Please insert coins: ")
    total = int(input("Please insert quarters: "))*0.25
    total+= int(input("Please insert dimes: "))*0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
def transaction_success(money_inserted, cost):
    if money_inserted< cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change =round(money_inserted - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit +=cost
        return True

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on = True
while is_on:
    response = input("What would you like? (espresso/latte/cappuccino): ")
    if response == "report":
        print(f"Water: {resources.get('water')}ml \n Milk: {resources.get('milk')}ml \n Coffee: {resources.get('coffee')}gr \n"
              f"money: {profit}$")
    elif response == "off":
        is_on = False
    else:
        name = MENU[response]
        if sufficient_ingredients(name["ingredients"]):
            payment = coins_count()
            if transaction_success(payment, name["cost"]):
                make_coffee(response, name["ingredients"])
