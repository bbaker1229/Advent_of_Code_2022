#!/usr/bin/env python3

# Define counter
count = 0  # count the number of pairs fully contained in the other

# Read input file
with open("puzzle_input.txt") as f:
    for line in f:
        elf1, elf2 = line.split(',')  # split the line into data for two elves
        elf1 = elf1.split('-')  # split the first elf data into first and second values
        elf2 = elf2.split('-')  # split the second elf data into first and second values
        test = ['B', 'B']  # initialize the test list
        # Test low value
        if int(elf1[0]) > int(elf2[0]):  # Record if the second elf has the lower value
            test[0] = 'E2'
        elif int(elf1[0]) < int(elf2[0]):  # Record if the first elf has the lower value
            test[0] = 'E1'
        # Test high value
        if int(elf1[1]) > int(elf2[1]):  # Record if the first elf has the higher value
            test[1] = 'E1'
        elif int(elf1[1]) < int(elf2[1]):  # Record if the second elf has the higher value
            test[1] = 'E2'
        # count the pair if the two values in the test list are the same or if one contains 'B'
        if (test[0] == test[1]) or (test[0] == 'B') or (test[1] == 'B'):  
            count += 1

# Output data
print(f"The number of pairs fully contained in the other is: {count}")
