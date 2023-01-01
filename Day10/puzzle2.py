#!/usr/bin/env python3

# Define required functions
def tick_record(clock, X_reg):
    """
    Function to determine the character to print
    """
    adj_clock = clock % 40  # Adjust the clock depending on which line we are printing
    distance = X_reg - adj_clock  # Find the distance between the sprite and then clock tick
    if distance in [-1, 0, 1]:  # Only print '#' if the distance is -1, 0, or 1
        return '#'
    else:
        return '.'

def print_output(reg_tracking):
    """
    Function to print the output
    """
    for key, value in reg_tracking.items():  # Iterate through the reg_tracking dict
        if key % 40 != 0:  # Determine which line we are printing
            print(value, end="")  # for within line do no return
        else:
            print(value)  # Return to new line if we are done with this one

# Read input file
clock = 0  # Initialize the clock
X_reg = 1  # Initialize the register
reg_tracking = dict()  # Initialize register tracking
with open("puzzle_input.txt") as f:  # Open input file
    for line in f:  # Get a line of the file
        line = line.split()  # Split the line on spaces
        if line[0] == 'noop':  # Noop, set the clock and record the reg value
            char_to_print = tick_record(clock, X_reg)  # Get the char to print
            clock += 1  # Iterate the clock
            reg_tracking[clock] = char_to_print  # Record the char
        if line[0] == 'addx':  # Addx, set the clock twice and record, set reg at end
            char_to_print = tick_record(clock, X_reg)  # Get the char to print
            clock += 1  # Iterate the clock
            reg_tracking[clock] = char_to_print  # Record the char
            char_to_print = tick_record(clock, X_reg)  # Get the char to print
            clock += 1  # Iterate the clock
            reg_tracking[clock] = char_to_print  # Record the char
            X_reg += int(line[1])  # Finally set a new X_reg value

# Print the output
print_output(reg_tracking)
