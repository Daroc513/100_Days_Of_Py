#!/usr/bin/env python3

import os
from secret_auction_ascii import logo

# Display welcome message
print(logo)
print("###########################-A Daroc Production: The Secret Auction-#######################")

# Initialize bids dictionary and bidding_finish flag
bids = {}
bidding_finish = False

# Function to determine the highest bidder
def highest_bidder(bidding_record):
    global bidding_finish
    highest_bid = 0
    winner = ""
    
    # Iterate through the bidding records to find the highest bidder
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    # Display the highest bidder and their bid
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
    # Ask the user if they want to start a new secret auction or quit
    result = input("Type 'y' to start a new secret auction or Type 'n' to quit: ").lower()
    
    # Process user input
    if result == "n":
        bidding_finish = True
        print("Goodbye!")
    elif result == "y":
        print("A new secret auction has begun!")
        bidding_finish = False

# Main bidding loop
while not bidding_finish:
    # Get bidder's name and bid amount
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    
    # Store the bid in the bids dictionary
    bids[name] = price
    
    # Ask if there are any other bidders
    more_bidders = input("Are there any other bidders? Type 'y' for yes and 'n' for no: ").lower()
    
    # Process user input
    if more_bidders == "n":
        bidding_finish = True
        highest_bidder(bids)
    elif more_bidders == "y":
        os.system('cls')  # Clear the screen (may need adjustment based on your OS)
