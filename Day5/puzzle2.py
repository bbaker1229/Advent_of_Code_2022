#!/usr/bin/env python3
from collections import deque

# Define the cargo data structure
# Use a deque for each stack
cargo = list()
for i in range(9):
    cargo.append(deque())

with open("puzzle_input.txt") as f:
    for line in f:
        if '[' in line:  # We are in the top of the file defining the stacks.
            for i in range(9):
                crate = line[i*4 + 1]  # Find the value of the crate for each location
                if crate != ' ':
                    cargo[i].appendleft(crate)  # If this is a letter then add to the deque location.
        elif 'move' in line:  # We are in the second section defining the moves.
            line = line.split()  # split the line on spaces
            quantity = int(line[1])  # find the quantity of crates moved
            from_index = int(line[3]) - 1  # find the index of the stack crates are moved from
            to_index = int(line[5]) - 1  # find the index of the stack crates are moved to
            crane = deque()
            for i in range(quantity):
                temp = cargo[from_index].pop()  # For the number of crates moved, pop the top from the first location
                crane.appendleft(temp)  # append left into the crane for these crates
            for i in range(quantity):
                temp = crane.popleft()  # pop left from the crane for these crates
                cargo[to_index].append(temp)  # append to the top of the second location.

# Create the string for the output by finding the top crate for each stack
output = ''
for i in range(9):
    output += cargo[i].pop()

# Output data
print(f"The crates on the top of each stack are: {output}.")
