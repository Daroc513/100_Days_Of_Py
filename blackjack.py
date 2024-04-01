import random
import os
from blackjack_art import logo  # Importing the logo from another module

print("\n*****************-A Daroc Production: Blackjack-************************")

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9 ,10 ,10, 10]  # Define the cards in the deck
    card = random.choice(cards)  # Randomly select a card from the deck
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    
    if sum(cards) == 21 and len(cards) == 2:  # If the player/dealer gets a blackjack (21 with only 2 cards)
        return 0  # Return 0 to signify a blackjack
    
    if 11 in cards and sum(cards) > 21:  # If there's an Ace in the hand and total score is greater than 21
        cards.remove(11)  # Remove the Ace (11 points)
        cards.append(1)  # Add an Ace (1 point) to avoid busting
    
    return sum(cards)  # Return the total score of the cards

def compare(user_score, computer_score):
    """Compare the scores of the player and the computer and determine the winner."""
    if user_score > 21 and computer_score > 21:  # If both player and computer bust
        return "You went over. You lose"
    if user_score == computer_score:  # If both player and computer have the same score
        return "Draw"
    elif computer_score == 0:  # If the computer has a blackjack
        return "Lose, opponent has Blackjack"
    elif user_score == 0:  # If the player has a blackjack
        return "Win, with Blackjack"
    elif user_score > 21:  # If the player busts
        return "You went over, You lose"
    elif computer_score > 21:  # If the computer busts
        return "Opponent went over, you win"
    elif user_score > computer_score:  # If the player's score is higher than the computer's score
        return "You win"
    else:
        return "You lose"  # If none of the above conditions are met, player loses

def play_game():
    """Function to start and play a game of blackjack."""

    print(logo)  # Print the game logo

    user_cards = []  # List to hold the player's cards
    computer_cards = []  # List to hold the computer's cards
    is_game_over = False  # Boolean to track if the game is over

    # Deal initial cards to the player and computer
    for _ in range(2):
        user_cards.append(deal_card())  # Add a card to the player's hand
        computer_cards.append(deal_card())  # Add a card to the computer's hand

    # Loop until the game is over
    while not is_game_over:

        user_score = calculate_score(user_cards)  # Calculate the player's score
        computer_score = calculate_score(computer_cards)  # Calculate the computer's score
        print(f"Your cards: {user_cards}, current score: {user_score}")  # Display player's cards and score
        print(f"Computer's first card: {computer_cards[0]} ")  # Display computer's first card

        # Check if the game should end based on player's actions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True  # End the game if player busts or gets a blackjack
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")  # Ask player if they want another card
            if user_should_deal == "y":
                user_cards.append(deal_card())  # Deal another card to the player
            else:
                is_game_over = True  # End the game if player chooses to pass

    # Computer's turn to draw cards
    while computer_score != 0 and computer_score < 17:  # Keep drawing cards until computer's score is at least 17
        computer_cards.append(deal_card())  # Deal another card to the computer
        computer_score = calculate_score(computer_cards)  # Recalculate computer's score

    # Display final hands and scores, and determine the winner
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))  # Compare scores and determine the winner

    # Ask if the player wants to play another game
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        os.system('cls')  # Clear the screen
        play_game()  # Start a new game if player chooses to continue

play_game()  # Start the game
