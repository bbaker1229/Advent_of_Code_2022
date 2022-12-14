#!/usr/bin/env python3
import numpy as np

# Define counter
count = 0  # count the number of pairs fully contained in the other

# Read input file
with open("puzzle_input.txt") as f:
    for line in f:
        elf1, elf2 = line.split(',')  # split the line into data for two elves
        elf1 = elf1.split('-')  # split the first elf data into first and second values
        elf1 = [int(i) for i in elf1]  # cast as integers
        elf2 = elf2.split('-')  # split the second elf data into first and second values
        elf2 = [int(i) for i in elf2]  # cast as integers
        values = list(np.unique(elf1 + elf2))  # Find the unique values
        test = list()  # initialize the test list
        for value in values:  # loop over each value
            if value == elf1[0]:  # add if in elf1
                test.append('1')
            if value == elf2[0]:  # add if in elf2
                test.append('2')
            if len(test) == 2:  # check if two values have been added to the test list
                count += 1
                break  # count and break if true
            if value == elf1[1]:  # Remove if in elf1
                test.remove('1')
            if value == elf2[1]:  # Remove if in elf2
                test.remove('2')

# Output data
print(f"The number of over lapping pairs is: {count}")
