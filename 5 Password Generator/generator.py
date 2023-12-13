import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
pwd_length = int(input("How long should your password be?\n"))
pwd_nums = int(input("How many numbers should be included?\n"))
pwd_symbols = int(input("How many symbols should be included?\n"))

letter_count = pwd_length - pwd_nums - pwd_symbols
new_password = ""
for letter in range(1,letter_count + 1):
    new_password += random.choice(letters)
for number in range(1,pwd_nums + 1):
    new_password += random.choice(numbers)
for symbol in range(1,pwd_symbols + 1):
    new_password += random.choice(symbols)

new_new_password = ''.join(random.sample(new_password,len(new_password)))
print(new_new_password)
