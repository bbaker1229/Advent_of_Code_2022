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

# First check visable trees from the left side of the forest
check_from_left = list()  # Create a list to collect the data
for i in range(rows):  # Start with a row of data
    max = -1  # initialize the max value of the trees seen
    temp = list()  # initialize a list to save the row of visability data
    for j in range(cols):  # Loop through the columns
        if forest[i, j] > max:  # If this tree is larger than the max value it can be seen.  
            temp.append(1)  # Add a 1 value to the dataset
            max = forest[i, j]  # Update the max value needed to be seen
        else:
            temp.append(0)  # Otherwise, the tree is not seen and enter a 0 in the dataset
    check_from_left.append(temp)  # Add the line to the data
check_from_left = np.matrix(check_from_left)  # Create a matrix from the data

# Check visable trees from the right side of the forest
check_from_right = list()  # Create a list to collect the data
for i in range(rows):  # Start with a row of data
    max = -1  # initialize the max value of the trees seen
    temp = list()  # initialize a list to save the row of visability data
    for j in range(cols):  # Loop through the columns
        if forest[i, -(j + 1)] > max:  # If this tree is larger than the max value it can be seen.
            temp.insert(0, 1)  # Add a 1 value to the dataset
            max = forest[i, -(j + 1)]  # Update the max value needed to be seen
        else:
            temp.insert(0, 0)  # Otherwise, the tree is not seen and enter a 0 in the dataset
    check_from_right.append(temp)  # Add the line to the data
check_from_right = np.matrix(check_from_right)  # Create a matrix from the data

# Check visable trees from the top side of the forest
check_from_top = list()  # Create a list to collect the data
for j in range(cols):  # Start with a column of data
    max = -1  # initialize the max value of the trees seen
    temp = list()  # initialize a list to save the column of visability data
    for i in range(rows):  # Loop through the rows
        if forest[i, j] > max:  # If this tree is larger than the max value it can be seen.
            temp.append(1)  # Add a 1 value to the dataset
            max = forest[i, j]  # Update the max value needed to be seen
        else:
            temp.append(0)  # Otherwise, the tree is not seen and enter a 0 in the dataset
    check_from_top.append(temp)  # Add the line to the data
check_from_top = np.matrix(check_from_top)  # Create a matrix from the data
check_from_top = np.transpose(check_from_top)  # Transpose this matrix

# Check visable trees from the bottom side of the forest
check_from_bottom = list()  # Create a list to collect the data
for j in range(cols):  # Start with a column of data
    max = -1  # initialize the max value of the trees seen
    temp = list()  # initialize a list to save the column of visability data
    for i in range(rows):  # Loop through the rows
        if forest[-(i + 1), j] > max:  # If this tree is larger than the max value it can be seen.
            temp.insert(0, 1)  # Add a 1 value to the dataset
            max = forest[-(i + 1), j]  # Update the max value needed to be seen
        else:
            temp.insert(0, 0)  # Otherwise, the tree is not seen and enter a 0 in the dataset
    check_from_bottom.append(temp)  # Add the line to the data
check_from_bottom = np.matrix(check_from_bottom)  # Create a matrix from the data
check_from_bottom = np.transpose(check_from_bottom)  # Transpose this matrix

# Find the visable forest by added each of the above matrices element-wise
visable_forest = check_from_left + check_from_bottom + check_from_right + check_from_top

# Determine the number of visable trees in the forest
count = 0  # initialize the counter
for i in range(rows):  # Loop through the rows
    for j in range(cols):  # Loop through the columns
        if visable_forest[i, j] > 0:
            count += 1  # If the tree is greater than 0 then it is visable.  Count it.

# Output
print(f"The number of visable trees is: {count}.")
