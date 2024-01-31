#name=input("What is your name? ")

"""day 8 practice materials"""

def greet():
    """base function work"""
    print("Good Morning")
    print("This day seems a little bit cold")
    print("Make sure that you dress warmly to leave the house")

def greet_with_name(name):
    """added one parameter"""
    print(f"Good Morning {name}")
    print("This day seems a little bit cold")
    print("Make sure that you dress warmly to leave the house")

#greet_with_name("Don")

def greet_with_multiple_parameters(name,location):
    """added multiple parameters"""
    print(f"Hello {name}")
    print(f"What is it like in {location}")

#positional arguments
# greet_with_multiple_parameters("Don","PA")
# keyword arguments
greet_with_multiple_parameters(location="England",name="April")
