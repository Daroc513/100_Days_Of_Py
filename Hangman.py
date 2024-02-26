#!/usr/bin/env python3

import os
# Import the 'os' module to interact with the operating system to clear the screen after every guess

import random
# Import the 'random' module for generating random choices

from Hangman_words import word_list
# Import the 'word_list' variable from the 'Hangman_words' directory

from Hangman_art import logo, stages
# Import the 'logo' and 'stages' variables from the 'Hangman_art' directory

chosen_word = random.choice(word_list)
# Randomly select a word from the word list and assign it to 'chosen_word'

word_length = len(chosen_word)
# Determine the length of the chosen word and assign it to 'word_length'

end_of_game = False
# Initialize a variable to track whether the game has ended

lives = 6
# Set the initial number of lives for the player

print(logo)
# Print the Hangman game logo

print("*******************-A Daroc production-*********************************\n")

display = []
# Initialize an empty list to store the current state of the word being guessed

for _ in range(word_length):
    display += "_"
# Populate the 'display' list with underscores representing each letter of the word

print(display)
# Print the initial state of the word as underscores

while not end_of_game:
    # Begin the main game loop

    guess = input("Guess a letter:").lower()
    # Prompt the player to guess a letter and convert the input to lowercase

    os.system('cls')
    # Clear the console screen to hide the previous guesses

    if guess in display:
        print(f"You've already guessed {guess}")
        # Inform the player if the guessed letter has already been guessed

    for position in range(word_length):
        letter = chosen_word[position]
        # Iterate through each position in the chosen word

        if letter == guess:
            display[position] = letter
            # Update the display if the guessed letter matches a letter in the word

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")

        lives -= 1
        # Decrement the number of lives if the guessed letter is not in the word

        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"The word is {chosen_word}!")
            # End the game if the player runs out of lives

    print(f"{' '.join(display)}")
    # Print the current state of the word with spaces between each letter

    if "_" not in display:
        end_of_game = True
        print(f"The word is {chosen_word}!")
        print("You win!")
        # End the game if the player successfully guesses the word

    from Hangman_art import stages
    print(stages[lives])
    # Print the visual representation of the Hangman based on the remaining lives