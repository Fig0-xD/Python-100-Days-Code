from assets import MENU, resources
from art import logo


def refill():

    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100

    print("\nMachine resources are refilled 👌")


def report():

    print("\n\tREPORT")
    print("Resources left:")
    print(f"- Water: {resources['water']} mL")
    print(f"- Milk: {resources['milk']} mL")
    print(f"- Coffee: {resources['coffee']} g")

    print(f"\nMoney earned: ${resources['money']}")


def deplete_resources(coffee_type):

    resources['water'] -= MENU[coffee_type]['ingredients']['water']
    resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
    resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']


def check_resources(coffee_type):

    resources_status = [resources['water'] >= MENU[coffee_type]['ingredients']['water'],
                        resources['milk'] >= MENU[coffee_type]['ingredients']['milk'],
                        resources['coffee'] >= MENU[coffee_type]['ingredients']['coffee']]

    return resources_status


def insert_money(coffee_type):

    resources_status = check_resources(coffee_type)

    if False in resources_status:
        print("\nSorry 🤕, the machine is short on:")
        if not resources_status[0]:
            print("- water")
        if not resources_status[1]:
            print("- milk")
        if not resources_status[2]:
            print("- coffee")
    else:

        print("\nPlease insert coins only:")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        dollars = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

        if dollars >= MENU[coffee_type]['cost']:

            deplete_resources(coffee_type)
            resources['money'] += MENU[coffee_type]['cost']

            print(f"\nTake your change: ${round(dollars - MENU[coffee_type]['cost'], 2)}")
            print(f"Here is your {MENU[coffee_type]['name']} ☕, ENJOY! 😊\n")

        else:
            print("Sorry that's not enough money ☹ Money refunded.")


def machine():

    while True:

        print("\n\tMENU")
        print(f"E - Espresso: ${MENU['e']['cost']}")
        print(f"L - Latte: ${MENU['l']['cost']}")
        print(f"C - Cappuccino: ${MENU['c']['cost']}")

        coffee_type = input("What would you like?: ").lower()

        if coffee_type == "off":
            print("\nTurning OFF machine..... 😴")
            break
        elif coffee_type == "report":
            report()
        elif coffee_type == "refill":
            refill()
        elif coffee_type in ['e', 'l', 'c']:
            insert_money(coffee_type)
        else:
            print("\nOOPS!😵 Something went wrong")


if __name__ == '__main__':
    print(logo)
    machine()