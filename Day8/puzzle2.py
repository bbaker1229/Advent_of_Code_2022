#!/usr/bin/env python3
import numpy as np

# Read the input data
l = list()  # Create a list to hold data
with open('puzzle_input.txt') as f:
    for line in f:
        value = [*line.strip()]  # Strip the new line char
        value = [int(item) for item in value]  # Make values integers
        l.append(value)  # Append line to data list

# Create a numpy matrix
forest = np.matrix(l)
rows, cols = forest.shape  # Get the dimensions of the matrix
score = 0  # Initialize the high score value.

for row in range(rows):  # Loop through rows
    for col in range(cols):  # Loop through cols
        tree_size = forest[row, col]  # Find the size of the current tree
        # Check to the right of the tree
        index = col + 1
        count = 0
        while index < cols:
            if forest[row, index] < tree_size:
                count += 1
                index += 1
            elif forest[row, index] == tree_size:
                count += 1
                index = cols
            elif (forest[row, index] > tree_size) and (count == 0):
                count += 1
                index = cols 
            else:
                index = cols
        right_check = count 
        # Check to the left of the tree
        index = col - 1
        count = 0
        while index > -1:
            if forest[row, index] < tree_size:
                count += 1
                index -= 1
            elif forest[row, index] == tree_size:
                count += 1
                index = -1
            elif (forest[row, index] > tree_size) and (count == 0):
                count += 1
                index = -1 
            else:
                index = -1
        left_check = count 
        # Check to the bottom of the tree
        index = row + 1
        count = 0
        while index < rows:
            if forest[index, col] < tree_size:
                count += 1
                index += 1
            elif forest[index, col] == tree_size:
                count += 1
                index = rows
            elif (forest[index, col] > tree_size) and (count == 0):
                count += 1
                index = rows 
            else:
                index = rows
        bottom_check = count 
        # Check to the top of the tree
        index = row - 1
        count = 0
        while index > -1:
            if forest[index, col] < tree_size:
                count += 1
                index -= 1
            elif forest[index, col] == tree_size:
                count += 1
                index = -1
            elif (forest[index, col] > tree_size) and (count == 0):
                count += 1
                index = -1
            else:
                index = -1
        top_check = count 
        temp_score = right_check * left_check * bottom_check * top_check
        if temp_score > score:
            score = temp_score

# Output
print(f"The largest scenic score possible is: {score}.")
