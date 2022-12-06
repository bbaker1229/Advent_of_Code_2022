#!/usr/bin/env python3

# Define variables
ELVES = dict()  # Use a dictonary to hold values of calories with the elf number used as the key 
elf_number = 1  # Set the first elf number
total = 0  # Initialize the calorie count

# Read input file
with open("puzzle_input.txt") as f:
    for line in f:
        if line != "\n":  # Line is not a blank line so continue counting elf calories
            total += int(line)
        else:  # Line is blank, save calories and elf number to dictonary and reinitialize vars.
            ELVES[elf_number] = total
            total = 0
            elf_number += 1

# Output data
max_value = max(ELVES.values())
max_key = max(ELVES, key=ELVES.get)
print(f"The most calories are held by Elf number: {max_key} who is carrying {max_value} calories.")
