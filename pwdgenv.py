import os
os.system('clear')
import random
uppercase_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
lowercase_letters = uppercase_letters.lower()
digits = "1234567890"
symbols = "!@#$%^&*(){}:><? "
print("This is a password generator made in python \n")
a = input("Do you want to include upper case letters? \n Enter y for yes and n for no \n")
if a == 'y':
    upper = True
else:
    upper = False
b = input("Do you want to include lower case letters? ")
if b == 'y':
    lower = True
else:
    lower = False
c = input("Do you want to include digits? ")
if c == 'y':
    nums = True
else:
    nums = False
d = input("Do you want to include symbols? ")
if d == 'y':
    syms = True
else:
    syms = False
all = ""
if upper:
    all+=uppercase_letters
if lower:
    all+=lowercase_letters
if nums:
    all+=digits
if syms:
    all+=symbols
length = int(input("Enter length of password "))
password = "".join(random.sample(all , length))
print(password)

