#!/usr/bin/env python3
import numpy as np

# Represent a state as ['elevation_letter', (x_location, y_location)]
class Node:
    """
    Define a node class to store the state and path information.
    """
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state  # Save the state of the node
        self.parent = parent  # Save the node of the parent node
        self.action = action  # Save the action required to get here from the parent
        self.path_cost = path_cost  # Save the steps required to get here
        self.depth = 0  # Save the depth of this node
        if parent:  # If this is a new node record the correct depth
            self.depth = parent.depth + 1

def possible_actions(state, gboard):
    """
    Define a function that returns the possible actions from the current state.
    """
    elevation_letter = state[0]  # Get the current elevation letter
    if elevation_letter == 'S':  # If this is the initial state then set the starting letter to 'a'
        elevation_letter = 'a'
    loc = state[1]  # Get the current location
    row_max = gboard.shape[0]  # Get the max number of rows in the game board
    col_max = gboard.shape[1]  # Get the max number of columns in the game board
    actions = []  # Initialize the action list.
    # Check if we can go up
    if (loc[0] - 1) >= 0:  # Make sure we do not go off the board on top
        new_letter = gboard[loc[0] - 1][loc[1]]  # Get the letter of this spot
        if (new_letter == 'E' and elevation_letter == 'z'):
            actions.append('Up')  # If we are currently on 'z' and the next is 'E' record the action
        elif ((new_letter != 'E') and ((chr(ord(elevation_letter) + 1) == new_letter) or (new_letter <= elevation_letter))):
            actions.append('Up')  # If the new letter is not 'E' and the new letter is one greater or any lower than the current letter record
    # Check if we can go down
    if (loc[0] + 1) < row_max:  # Make sure we do not go off the board on the bottom
        new_letter = gboard[loc[0] + 1][loc[1]]  # Get the letter of this spot
        if (new_letter == 'E' and elevation_letter == 'z'):
            actions.append('Down')  # If we are currently on 'z' and the next is 'E' record the action
        elif ((new_letter != 'E') and ((chr(ord(elevation_letter) + 1) == new_letter) or (new_letter <= elevation_letter))):
            actions.append('Down')  # If the new letter is not 'E' and the new letter is one greater or any lower than the current letter record
    # Check if we can go left
    if (loc[1] - 1) >= 0:  # Make sure we do not go off the board on the left
        new_letter = gboard[loc[0]][loc[1] - 1]  # Get the letter of this spot
        if (new_letter == 'E' and elevation_letter == 'z'):
            actions.append('Left')  # If we are currently on 'z' and the next is 'E' record the action
        elif ((new_letter != 'E') and ((chr(ord(elevation_letter) + 1) == new_letter) or (new_letter <= elevation_letter))):
            actions.append('Left')  # If the new letter is not 'E' and the new letter is one greater or any lower than the current letter record
    # Check if we can go right
    if (loc[1] + 1) < col_max:  # Make sure we do not go off the board on the right
        new_letter = gboard[loc[0]][loc[1] + 1]  # Get the letter of this spot
        if (new_letter == 'E' and elevation_letter == 'z'):
            actions.append('Right')  # If we are currently on 'z' and the next is 'E' record the action
        elif ((new_letter != 'E') and ((chr(ord(elevation_letter) + 1) == new_letter) or (new_letter <= elevation_letter))):
            actions.append('Right')  # If the new letter is not 'E' and the new letter is one greater or any lower than the current letter record
    return actions

def distance(state, target):
    """
    Define a heuristic for the Astar search to work.  
    Use radial distance.
    """
    current_location = state[1]  # Get the current location
    target_location = target[1]  # Get the target location
    return np.sqrt((current_location[0] - target_location[0]) * (current_location[0] - target_location[0]) + (current_location[1] - target_location[1]) * (current_location[1] - target_location[1]))

def child_node(parent, action, gboard):
    """
    Define a function that returns the resulting node for a given action 
    from a defined state.
    """
    pstate = parent.state  # Get the parent state
    parent_letter = pstate[0]  # Get the elevation letter for the parent state
    loc = pstate[1]  # Get the parent location
    child_loc = loc  # Set the child_location as the parent location if we don't move
    child_letter = parent_letter  # Set the child_letter as the parent letter if we don't move
    if action == 'Up':  
        child_loc = (loc[0] - 1, loc[1])  # Set the child location
        child_letter = gboard[child_loc[0]][child_loc[1]]  # Set the child letter
    if action == 'Down':
        child_loc = (loc[0] + 1, loc[1])  # Set the child location
        child_letter = gboard[child_loc[0]][child_loc[1]]  # Set the child letter
    if action == 'Left':
        child_loc = (loc[0], loc[1] - 1)  # Set the child location
        child_letter = gboard[child_loc[0]][child_loc[1]]  # Set the child letter
    if action == 'Right':
        child_loc = (loc[0], loc[1] + 1)  # Set the child location
        child_letter = gboard[child_loc[0]][child_loc[1]]  # Set the child letter
    newstate = [child_letter, child_loc]  # Create the new child state
    child = Node(newstate, parent, action, parent.path_cost + 1)  # Create the new child node
    return child

def astar(initial_state, target_state, gboard):
    """
    Define a function using Astar search to solve using the initial state,
    the target state, and the game board.
    """
    initial_node = Node(initial_state)  # Create the initial node
    frontier = [initial_node]  # Create a list to use as next possible states to move into
    reached = [initial_node.state]  # Keep track of the states that we have visited to prevent us from returning
    value = distance(initial_node.state, target_state)  # Find the distance from the initial node to the target
    rank = [initial_node.path_cost + value]  # Record this value in a rank list
    while frontier:  # Loop through the frontier list
        ind = rank.index(min(rank))  # Find the index of the next closest node
        this_node = frontier.pop(ind)  # Get the node
        rank.pop(ind)  # Throw out that rank
        if this_node.state == target_state:  # If this node's state is the target we are done
            return this_node
        actions = possible_actions(this_node.state, gboard)  # Get the possible actions from this node
        for action in actions:  # Loop through all the actions
            child = child_node(this_node, action, gboard)  # Get the child node for this action
            if child.state not in reached:  # Record this new state if it is one that we have not yet visited
                value = distance(child.state, target_state)  # Find the distance from this node to the target
                frontier.append(child)  # Add this node to the frontier
                rank.append(child.path_cost + value)  # Add the rank for this node to the rank list
                reached.append(child.state)  # Add this node's state to the reached list
    return []

# Read in the game board
all_lines = list()  # Initialize a list to hold all of the lines 
with open("puzzle_input.txt") as f:  # Open input file
    for line in f:  # Get a line of the file
        if line.endswith('\n'):  # If the line ends with a new line character then remove it
            line = line.removesuffix('\n')
        all_lines.append(list(line))  # Append all the lines together

game_board = np.array(all_lines, dtype=str)  # Create the game board using the lines as a numpy array
target_location = np.where(game_board == 'E')  # Find the location of the target
target_location = (target_location[0][0], target_location[1][0])  # Set the target location using only integers
target_state = ['E', target_location]  # Set the target state

# This is not the most elegant method, but gets the job done
distance_list = list()  # Initialize a list to store the distances
for i in range(game_board.shape[0]):  # Loop through all x values of the game board
    for j in range(game_board.shape[1]):  # Loop through all y values of the game board
        if game_board[i][j] == 'a':  # If the letter in that location is an 'a' solve
            starting_location = (i, j)  # Set the start location
            starting_state = ['a', starting_location]  # Set the start state

            # Find the solution from the starting state to the target state using A* search
            solution = astar(starting_state, target_state, game_board)
            if solution != list():  # If a solution is found record the depth
                distance_list.append(solution.depth)

#Output data
min_value = min(distance_list)  # Find the min value
print(f"The fewest number of steps from an 'a' starting position is: {min_value}.")
