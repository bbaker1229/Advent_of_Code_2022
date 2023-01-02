#!/usr/bin/env python3
import numpy as np

def calm_down(worry_level):
    """
    This is the 'calm_down' function as described
    """
    return np.floor(worry_level / 3)  # return the lowest integer value of worry / 3

class Monkey:
    """
    Create a class to describe the monkeys and their actions
    """
    def __init__(self):
        """
        Initialize the monkey class
        """
        self._items_holding = list()  # Start a list to hold the items the monkey holds
        self._operation = list()  # Start a list to hold the operation details the monkey uses
        self._test = 0  # Initialize a test operation that is used as a divisor
        self._if_true = -1  # Throw to this monkey if the test is true
        self._if_false = -1  # Throw to this monkey if the test if false
    def inspect(self):
        """
        Define a method to use when the monkey inspects an object
        """
        return self._items_holding.pop(0)  # Pop the first item from the list of items the monkey holds
    def change_worry_level(self, worry_level):
        """
        Define a method to use when worrying about what the monkey is holding
        """
        if self._operation[1] == 'old':
            value = worry_level  # If the old value of worry is used set it here
        else:
            value = int(self._operation[1])  # Define the value to use in the operation
        if self._operation[0] == '+':
            return (worry_level + value)  # Return new value if addition is used
        elif self._operation[0] == '*':
            return (worry_level * value)  # Return new value if multiplication is used
    def test_item(self, worry_level):
        """
        Define a method to use to determine which monkey to throw to
        """
        check = worry_level % self._test  # Define the check method
        if check == 0:
            return self._if_true  # Throw to this monkey if true
        else:
            return self._if_false  # Throw to this monkey if false

def one_round(monkey_pack, counter_list):
    """
    Define a function to complete one round of play
    """
    for monkey_number, monkey in monkey_pack.items():  # Loop through all monkeys
        counter = counter_list[monkey_number]  # Get the counter to use for this monkey
        number_of_items = len(monkey._items_holding)  # Get the number of items to loop through
        for i in range(number_of_items):  # Loop through all items
            worry_level = monkey.inspect()  # The monkey inspects the item
            counter += 1  # Increase the counter
            worry_level = monkey.change_worry_level(worry_level)  # Update the worry level
            worry_level = calm_down(worry_level)  # Calm down
            item_goes_to = monkey.test_item(worry_level)  # Determine the new monkey to send to
            monkey_pack[item_goes_to]._items_holding.append(int(worry_level))  # Append to the new monkeys list
        counter_list[monkey_number] = counter  # Put the counter away.

monkey_pack = dict()  # Initialize a monkey pack
current_monkey = -1  # Set the current monkey value
with open("puzzle_input.txt") as f:  # Open input file
    for line in f:  # Get a line of the file
        if "Monkey" in line:  # If Monkey is in the line this is a new monkey
            line = line.split()  # Split the line on spaces
            current_monkey = int(line[1].replace(":", ""))  # Set the current monkey number
            new_monkey = Monkey()  # Create a new monkey
            monkey_pack[current_monkey] = new_monkey  # Add the new monkey to the monkey pack
        if "items" in line:  # If 'items' is in the line this is a line describing the items held
            line = line.split()  # Split the line on spaces
            number_of_items = len(line) - 2  # Determine the number of items held
            monkey = monkey_pack[current_monkey]  # Get the monkey to assign to
            for i in range(number_of_items):  # Loop through all items to add
                monkey._items_holding.append(int(line[i + 2].replace(",", "")))  # Add the items to the list
        if "Operation" in line:  # If 'Operation' is in the line this is defining the operation to use
            line = line.split()  # Split the line on spaces
            monkey = monkey_pack[current_monkey]  # Get the monkey to assign to
            monkey._operation = line[4:]  # Add the operation to the monkey
        if "Test" in line:  # If 'Test' is in the line this defines the test value
            line = line.split()  # Split the line on spaces
            monkey = monkey_pack[current_monkey]  # Get the monkey to assign to
            monkey._test = int(line[-1])  # Set the test value
        if "If true" in line:  # If 'If true' is in the line this defines the monkey to send to if true
            line = line.split()  # Split the line on spaces
            monkey = monkey_pack[current_monkey]  # Get the monkey to assign to
            monkey._if_true = int(line[-1])  # Set the true value
        if "If false" in line:  # If 'If false' is in the line this defines the monkey to send to if false
            line = line.split()  # Split the line on spaces
            monkey = monkey_pack[current_monkey]  # Get the monkey to assign to
            monkey._if_false = int(line[-1])  # Set the false value

# Initialize the counter
counter_list = list()  # Create a list to hold the counters
for monkey_number, monkey in monkey_pack.items():  # Loop through all monkeys to set one counter per monkey
    counter_list.append(0)  # Initialize the counter to zero

# Run through all rounds of play
for i in range(20):  # Loop through 20 rounds
    one_round(monkey_pack, counter_list)

# Determine the amount of monkey business
most_active = max(counter_list)  # find the most active monkey
index = counter_list.index(most_active)  # find the index of the most active monkey
counter_list.pop(index)  # Remove the most active monkey
second_active = max(counter_list)  # find the second most active monkey
monkey_business = most_active * second_active  # Determine the amount of monkey business

# Output the data
print(f"The level of monkey business is: {monkey_business}.")
