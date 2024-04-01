#!/user/bin/env python

# Import the logo from the 'caesarcipher_asci' module
from caesarcipher_asci import logo
# Print the logo to the console
print(logo)
# Print a header message
print("***************-A DaRoc Production: Caesar Cypher Message Encoder & Decoder!-****************************\n")

# List variable with a list to define the alphabet for use in the Caesar cipher
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]

# Function to perform the Caesar cipher
def caesar(start_text, shift_amount, cipher_direction):
    # Initialize an empty string for the final result
    end_text = ""
    # Adjust the shift amount for decoding
    if cipher_direction == "decode":
        shift_amount *= -1
    # Iterate through each character in the input text
    for char in start_text:
        # Check if the character is in the alphabet
        if char in alphabet:
            # Get the position of the character in the alphabet
            position = alphabet.index(char)
            # Calculate the new position after applying the shift
            new_position = position + shift_amount
            # Append the new character to the result string
            end_text += alphabet[new_position]
        else:
            # If the character is not in the alphabet, keep it unchanged
            end_text += char
    # Print the result
    print(f"The {cipher_direction}d text is {end_text}")

# Variable to control the main loop
should_end = False
# Main loop for user interaction
while not should_end:
    # Get user input for the cipher direction
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Get user input for the text to be encoded/decoded
    text = input("Type your message:\n").lower()
    # Get user input for the shift amount
    shift = int(input("Type the shift number:\n"))
    
    # Ensure the shift is within the valid range
    shift = shift % 26

    # Call the caesar function with user inputs
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Ask the user if they want to go again
    result = input("Type 'y' if you want to go again. Otherwise type 'n'. \n").lower()
    if result == "n":
        should_end = True
        print("Goodbye")
