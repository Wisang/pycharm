# to test git push
# to test git push from mac
# to test push from windows again
# to test from mac again

# TODO: 1. print report
# TODO: 2. Turn Off for off
# TODO: 3. check if resource is sufficient
# TODO: 4. Process coins
# TODO: 5. Check transaction successful
# TODO: 6. Make Coffee

from data import MENU, resources
power_off = False
current_resources = resources
profit = 0.0


def print_report():
    print(f"water: {current_resources['water']}")
    print(f"milk: {current_resources['milk']}")
    print(f"coffee: {current_resources['coffee']}")
    print(f"money: {profit}")


def check_resource(user_choice):
    menu = user_choice
    ingredient = MENU[menu]["ingredients"]
    for item in ingredient:
        if current_resources[item] < ingredient[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    quarters = int(input("quarters: "))
    dimes = int(input("dimes: "))
    nickles = int(input("nickles: "))
    pennies = int(input("pennies: "))
    result = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return round(result, 2)


def update_resources(user_choice):
    for item in MENU[user_choice]['ingredients']:
        current_resources[item] -= MENU[user_choice]['ingredients'][item]


profit = 0


def do_transaction(choice):
    change = round(input_money - cost, 2)
    if change > 0:
        print(f"Here is ${change} dollars in change.")
    update_resources(choice)
    print(f"Here is your {choice}. Enjoy!")


while not power_off:
    input_money = 0.0
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        power_off = True
    elif order == "report":
        print_report()
    else:
        is_resource_sufficient = check_resource(order)
        if is_resource_sufficient:
            print("insert coins")
            input_money = process_coins()
            if input_money < MENU[order]["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                cost = MENU[order]["cost"]
                profit += cost
                do_transaction(order)