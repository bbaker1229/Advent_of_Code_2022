#!/usr/bin/env python3

signal = ''  # Define the empty signal
with open("puzzle_input.txt") as f:
    for line in f:
        signal += line  # Read in the signal

for i in range(len(signal)-13):
    temp = signal[i:i+14]  # Move through each group of 14 characters 
    if len(set(temp)) == 14:  # The first time that a set of 14 unique characters is found break
        break

# Output data
print(f"There are {i+14} characters that need to be processed before the first start of message.")
