#!/usr/bin/env python3

signal = ''  # Define the empty signal
with open("puzzle_input.txt") as f:
    for line in f:
        signal += line  # Read in the signal

for i in range(len(signal)-3):
    temp = signal[i:i+4]  # Move through each group of 4 characters 
    if len(set(temp)) == 4:  # The first time that a set of 4 unique characters is found break
        break

# Output data
print(f"There are {i+4} characters that need to be processed before the first packet.")
