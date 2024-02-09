"""Day 10 Final Project: Text based calculator"""
import calculator_art

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

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation to calculate: ")

answer = operations[operation_symbol](num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

