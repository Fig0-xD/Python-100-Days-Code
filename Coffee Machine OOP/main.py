from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def machine():

    money_machine= MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()

    while True:
        coffee = input(f"\nWhat would you like?({menu.get_items()}): ")

        if coffee == "off":
            print("Shutting down machine....")
            break

        elif coffee == "report":
            print("C - Coffee Maker\nM - Money Machine")
            choice = input("Enter here: ").lower()

            if choice == 'c':
                coffee_maker.report()
            else:
                money_machine.report()

        else:
            coffee = menu.find_drink(coffee)
            if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)


if __name__ == '__main__':
    machine()