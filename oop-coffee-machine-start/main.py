from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
while is_on:
    response = str(input("What would you like? (espresso/latte/cappuccino/): "))
    if response == "off":
        is_on = False
    elif response == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink1 = menu.find_drink(response)
        if coffee_maker.is_resource_sufficient(drink1) and money_machine.make_payment(drink1.cost):
            coffee_maker.make_coffee(drink1)






