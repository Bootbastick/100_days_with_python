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
offf = False


def coffee_machine(MENU, profit, resources):
    transaction = False
    not_enough_money = False
    total_count = 0
    reported = False
    question = input("What would you like? (espresso/latte/cappuccino): ").lower()


    def off():
        if question == "off":
            exit()
    if question == "off":
        off()


    def report():
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffe: {coffee}gr")
        print(f"Money: ${profit}")
        global reported
    if question == "report":
        report()
        reported = True


    if question == "espresso" and reported == False:
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        if resources["water"] <= 0 or resources["coffee"] <= 0:
            print("Sorry there is not enough resources.")
            enough_resources = False
        else:
            enough_resources = True
    elif question == question and reported == False:
        resources["water"] -= MENU[question]["ingredients"]["water"]
        resources["coffee"] -= MENU[question]["ingredients"]["coffee"]
        resources["milk"] -= MENU[question]["ingredients"]["milk"]
        if resources["water"] <= 0 or resources["coffee"] <= 0 or resources["milk"] <= 0:
            print("Sorry there is not enough resources.")
            enough_resources = False
        else:
            enough_resources = True
    elif question == "cappuccino" and reported == False:
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["espresso"]["ingredients"]["milk"]
        if resources["water"] <= 0 or resources["coffee"] <= 0 or resources["milk"] <= 0:
            print("Sorry there is not enough resources.")
            enough_resources = False
        else:
            enough_resources = True

    if reported == False:
        print("Please insert coins")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        total_count = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.05 * pennies
        if total_count < MENU[question]["cost"] and reported == False:
            print("Sorry that's not enough money. Money refunded.")
            not_enough_money = True
        elif total_count > MENU[question]["cost"] and reported == False:
            change = total_count - MENU[question]["cost"]
            print(f"Here is ${change} dollars in change.")
            transaction = True
            profit += total_count - change
        elif reported == False:
            transaction = True
            profit += total_count


        if transaction != False and enough_resources == True and reported == False and not_enough_money == False:
            print(f"Here is your {question}. Enjoy!")


    coffee_machine(MENU, profit, resources)
coffee_machine(MENU, profit, resources)