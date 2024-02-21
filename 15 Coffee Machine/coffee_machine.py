"""coffee machine program for day 15"""
import os
import kitchen


def clear_screen():
    """Function to clear screen before each output"""
    os.system("cls" if os.name == "nt" else "clear")

def print_report():
    """Prints Current Resources"""
    print(kitchen.resources)

def machine():
    """Machine Logic for making coffee"""
    selection = input("What would you like? (espresso/latte/cappuccino)").lower()
    if selection == 'off':
        return
    elif selection == 'report':
        print(print_report())
    elif 'espresso' in selection or 'latte' in selection or 'cappuccino' in selection:
        #attempt transaction
        print("Coming Soon")
    else:
        clear_screen()
        machine()

machine()
