# Day -- 5
# 10/18/2023
# Loops, for loop, while loop
# ----------------------------------------

# fruits = ["apples", "Bananas", ]

# for x in fruits:
#     print(x)

# target = int(input())  # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️

# # Write your code here 👇

# total = 0

# for number in range(target + 1):
#     if number % 2 == 0:
#         total += number

# print(total)

# for number in range(101):
#     if number % 5 == 0 & number % 3 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Fizz")
#     elif number % 3 == 0:
#         print("Buzz")
#     else:
#         print(number)

# ------------------------------------------------

#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(random.choice(letters))

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

string = []

print(random.shuffle(letters))

# picking a letter
for _ in range(nr_letters):
    string.append(random.choice(letters))

random.shuffle(string)

# picking a symbol
for _ in range(nr_symbols):
    string.append(random.choice(symbols))

random.shuffle(string)

# picking a number
for _ in range(nr_numbers):
    string.append(random.choice(numbers))

random.shuffle(string)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = (('').join(string))

print(f"Your password is:\n\n-->  {password}")
