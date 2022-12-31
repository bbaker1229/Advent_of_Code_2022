#!/usr/bin/env python3
import numpy as np

class Rope:
    """
    Create a class to track the head and tail of the rope.
    """
    def __init__(self):  # Initialize the rope
        self.head_location = (0, 0)  # Set the initial head location
        self.tail_location = (0, 0)  # Set the initial tail location
        self.tail_history = [(0, 0)]  # Set the initial tail history
    def update_tail(self):
        """
        Create a method to update the tail location
        """
        distance_x = self.head_location[0] - self.tail_location[0]  # Find the distance in the x direction
        distance_y = self.head_location[1] - self.tail_location[1]  # Find the distance in the y direction
        radius = np.sqrt(distance_x * distance_x + distance_y * distance_y)  # Find the radius
        if radius > np.sqrt(2):  # Only update the tait location if the head location travels far enough
            if distance_x > 0:  # For positive x, move to higher integer
                new_x = self.tail_location[0] + np.ceil(distance_x / 2)
            else:  # For negative x, move to lower integer
                new_x = self.tail_location[0] + np.floor(distance_x / 2)
            if distance_y > 0:  # For positive y, move to higher integer
                new_y = self.tail_location[1] + np.ceil(distance_y / 2)
            else:  # For negative y, move to lower integer
                new_y = self.tail_location[1] + np.floor(distance_y / 2)
            new_location = (int(new_x), int(new_y))  # Set the new location tuple
            self.tail_location = new_location  # Set the new tail location
            if new_location not in self.tail_history:  # If this is a new location, update
                self.tail_history.append(new_location)
    def move_up(self, steps):
        """
        Create a method to update the head and tail locations by moving up
        """
        for i in range(steps):  # Move a defined number of steps
            current_x = self.head_location[0]  # Get current x head location
            current_y = self.head_location[1]  # Get current y head location
            new_x = current_x  # Update x location
            new_y = current_y + 1  # Update y location
            self.head_location = (new_x, new_y)  # Set the new head location
            self.update_tail()  # Update the tail location
    def move_right(self, steps):
        """
        Create a method to update the head and tail locations by moving right
        """
        for i in range(steps):  # Move a defined number of steps
            current_x = self.head_location[0]  # Get current x head location
            current_y = self.head_location[1]  # Get current y head location
            new_x = current_x + 1  # Update x location
            new_y = current_y  # Update y location
            self.head_location = (new_x, new_y)  # Set the new head location
            self.update_tail()  # Update the tail location
    def move_left(self, steps):
        """
        Create a method to update the head and tail locations by moving left
        """
        for i in range(steps):  # Move a defined number of steps
            current_x = self.head_location[0]  # Get current x head location
            current_y = self.head_location[1]  # Get current y head location
            new_x = current_x - 1  # Update x location
            new_y = current_y  # Update y location
            self.head_location = (new_x, new_y)  # Set the new head location
            self.update_tail()  # Update the tail location
    def move_down(self, steps):
        """
        Create a method to update the head and tail locations by moving down
        """
        for i in range(steps):  # Move a defined number of steps
            current_x = self.head_location[0]  # Get current x head location
            current_y = self.head_location[1]  # Get current y head location
            new_x = current_x  # Update x location
            new_y = current_y - 1  # Update y location
            self.head_location = (new_x, new_y)  # Set the new head location
            self.update_tail()  # Update the tail location


# Initialize the starting rope
rope = Rope()
# Read the input data
with open('puzzle_input.txt') as f:  # Open input file
    for line in f:  # Get a line of the file
        line = line.split()  # Split the line using spaces
        direction = line[0]  # The direction is the first item in the line
        steps = int(line[1])  # The number of steps is the second item in the line
        if direction == 'U':  # Move up
            rope.move_up(steps)
        if direction == 'D':  # Move down
            rope.move_down(steps)
        if direction == 'R':  # Move right
            rope.move_right(steps)
        if direction == 'L':  # Move left
            rope.move_left(steps)

# Determine the number of unique locations the tail has visited
number_of_locations = len(rope.tail_history)

# Print the output
print(f"The number of unique locations visited by the tail is: {number_of_locations}.")
