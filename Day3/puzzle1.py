#!/usr/bin/env python3
import string

# Define variables
# Create a list of letters
letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
# Create a dictionary for the scores using the letters as the key.
scores = dict()
value = 0
for key in letters:
    value += 1
    scores[key] = value
total_score = 0  # initialize the total score

# Read input file
with open("puzzle_input.txt") as f:
    for line in f:
        text_length = len(line)  # Get the length of the string
        pack_length = int(text_length / 2)  # Find the pack split index
        pack1 = set(line[:pack_length])  # Define the values in pack1
        pack2 = set(line[pack_length:])  # Define the values in pack2
        value = list(pack1.intersection(pack2))[0]  # Find the character that is common to both
        value = scores[value]  # Find the score
        total_score += value  # Add to the total score

# Output data
print(f"The total sum is: {total_score}.")
