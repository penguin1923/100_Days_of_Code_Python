"""Day 10 Final Project: Text based calculator"""
import calculator_art

print(calculator_art.logo)

def add(n1,n2):
    """adds n1 to n2"""
    return n1 + n2

def subtract(n1,n2):
    """subtracts n2 from n1"""
    return n1 - n2

def multiply(n1,n2):
    """multiplies n1 and n2"""
    return n1 * n2

def divide(n1,n2):
    """divides n1 by n2"""
    return n1 / n2

operations = {"+":add,"-":subtract,"*":multiply,"/":divide}

def calculator():
    num1 = float(input("What is the first number? "))

    end_of_calculation = False

    while not end_of_calculation:
        for symbol in operations:
            print(symbol)
        valid_operation = False
        while not valid_operation:
            operation_symbol = input("Pick an operation to calculate: ")
            if operation_symbol in operations.keys():
                valid_operation = True

        num2 = float(input("What is the next number? "))

        answer = operations[operation_symbol](num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        would_continue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to to start a new calculation. ")

        if would_continue == 'y':
            num1 = answer
            continue
        elif would_continue == 'n':
            end_of_calculation = True
            calculator()
        else:
            end_of_calculation = True

calculator()
