#!/usr/bin/env python3

# Read input file
clock = 0  # Initialize the clock
X_reg = 1  # Initialize the register
reg_tracking = dict()  # Initialize register tracking
reg_tracking[clock] = X_reg  # set the first value in the tracking dictionary
with open("puzzle_input.txt") as f:  # Open input file
    for line in f:  # Get a line of the file
        line = line.split()  # Split the line on spaces
        if line[0] == 'noop':  # Noop, set the clock and record the reg value
            clock += 1
            reg_tracking[clock] = X_reg
        if line[0] == 'addx':  # Addx, set the clock twice and record, set reg at end
            clock += 1
            reg_tracking[clock] = X_reg
            clock += 1
            reg_tracking[clock] = X_reg
            X_reg += int(line[1])

# Determine the signal strength value
total = 0  # Initialize the total value
for key, value in reg_tracking.items():  # Loop through the dictionary
    if key in [20, 60, 100, 140, 180, 220]:  # Only record for certain values
        total += (key * value)  # Record the signal strength

# Print the output
print(f"The sum of the six signal strengths are: {total}.")
