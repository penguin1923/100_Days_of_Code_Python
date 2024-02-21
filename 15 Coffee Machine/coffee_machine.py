"""coffee machine program for day 15"""
import os
import kitchen
used_water = 0
used_milk = 0
used_coffee = 0
money_collected = 0
starting_resources = kitchen.resources
remaining_water  = starting_resources['water'] - used_water
remaining_milk = starting_resources['milk'] - used_milk
remaining_coffee = starting_resources['coffee'] - used_coffee

def clear_screen():
    """Function to clear screen before each output"""
    os.system("cls" if os.name == "nt" else "clear")

def print_report():
    """Prints Current Resources"""
    print(f"Water: {remaining_water}ml\nMilk: {remaining_milk}ml\nCoffee: {remaining_coffee}g\nMoney: {money_collected}")

def cashier(cost):
    """checks to make sure enough money is put in"""
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    change = (quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01)
    if change>=cost:
        global money_collected
        money_collected += cost
        exchange = round((change - cost),2)
        print(f"Here is your change ${exchange}")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_drink(choice):
    """attempts to make the drink requested."""
    recipe = kitchen.MENU[choice]
    needed_water = recipe["ingredients"]["water"]
    needed_milk = recipe["ingredients"]["milk"]
    needed_coffee = recipe["ingredients"]["coffee"]
    needed_money = recipe["cost"]
    global used_water
    global used_milk
    global used_coffee

    if (remaining_water>needed_water) and (remaining_milk>needed_milk) and (remaining_coffee>needed_coffee):
        if cashier(needed_money) is True:
            used_water =+ needed_water
            used_milk =+ needed_milk
            used_coffee =+ needed_coffee
            print(f"Here is your {choice}. Enjoy!!")
    elif remaining_water<needed_water:
        print("Sorry there is not enough water.")
    elif remaining_milk<needed_milk:
        print("Sorry there is not enough milk.")
    else:
        print("Sorry there is not enough coffee.")

def machine():
    """Machine Logic for making coffee"""
    selection = input("What would you like? (espresso/latte/cappuccino)").lower()
    if selection == 'off':
        return
    elif selection == 'report':
        print_report()
        machine()
    elif 'espresso' in selection or 'latte' in selection or 'cappuccino' in selection:
        #attempt transaction
        make_drink(selection)
        machine()
    else:
        clear_screen()
        machine()

machine()
