#!/usr/bin/env python3
####################################-A Daroc Production: Password Generator!-##############################################

import random #Imports the random module to select a random item from letters, numbers and symbols list.

#The following are 3 list that the module draws from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!") #Intro print function 

#input functions ask user to input number of letters,symbols and numbers
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = [] # Variable adds items(symbols,letters,numbers) to a list

#for loops allows user to select number of items from list
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters)) #Creates random letters

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols) #Creates random symbols

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers) #Creates random numbers

random.shuffle(password_list) #Shuffle function shuffles the users password list after inputing number of letters,symbols and numbers in a random order

password = ""
for char in password_list: #for each character in the password list, its added to the password variable
    password += char

print(f"Your password is: {password}") # F string prints users random password