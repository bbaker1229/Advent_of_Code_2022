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
line_number = 0  # Keep track of the line number
elf_group = list()  # initialize the elf group list

# Read input file
with open("puzzle_input.txt") as f:
    for line in f:
        elf_group.append(line.strip())  # add the line to the elf_group
        if (line_number % 3) == 2:  # if this is the third elf for the group find the score
            elf1 = set(elf_group[0])  # Find the pack for the first elf
            elf2 = set(elf_group[1])  # Find the pack for the second elf
            elf3 = set(elf_group[2])  # Find the pack for the third elf
            # Find the character that is common to all three
            value = list(elf1.intersection(elf2).intersection(elf3))[0]
            value = scores[value]  # Find the score
            total_score += value  # Add to the total score
            elf_group = list()  # Reinitialize the group list
        line_number += 1  # Update the line counter

# Output data
print(f"The total sum is: {total_score}.")
