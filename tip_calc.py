#!/usr/bin/env python3

#####################################-A Daroc Production: Tip Calculator-######################################################

# Introduction print function
print("Welcome to the tip calculator!")

# float and integer input functions for total bill, tip amount and number of people splitting bill
bill = float(input("What is your total bill? $"))

tip_amount = int(input("What percentage tip would you like to give? 10, 12, 15? "))

split = int(input("How many people are splitting the bill? "))

# Variable divides the total bill inputed by the number of people inputed then rounds to the second decimal
bill_split = round(bill / split, 2)

# Variable calculates the input on line 11 to a percentage
tip = 100 / tip_amount

# Variable calculates tip then rounds the tip to the 2nd decimal
total_tip = round(bill_split / tip, 2)

# Variable Adds the now split bill and the tip
bill_per = bill_split + total_tip

# Variable rounds the total bill plus tip per person to the second decimal
final_amount = round(bill_per, 2)

# Final print function with results
print(f"Each person will pay ${bill_split} bill, with a ${total_tip} tip, for a total of ${final_amount} per person.")