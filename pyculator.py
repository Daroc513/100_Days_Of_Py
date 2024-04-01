#!/usr/bin/env python3
from pyculator_ascii import logo
import os

print("*********************-A Daroc Production: Calculator-**************************")

#add
def add(n1, n2):
    return n1 +n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

#functions: Keys and Values
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#Recursive functions
def calculator():

    print(logo)
    num1 = float(input("Whats the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            os.system('cls')
            calculator()

calculator()