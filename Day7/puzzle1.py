#!/usr/bin/env python3

class Node:
    """
    Create a class to define the nodes for the directory tree.  
    """
    def __init__(self, name, size, node):  # Initialize a node
        self.parent = node  # Define the parent of the new node
        self.name = name  # Name the new node
        self.size = size  # Track the size of the node
        self.files = dict()  # Track the files in this node
        self.directories = dict()  # Track the directories in this node
    def add_directory(self, name):
        """
        Create method to add a directory to the node
        """
        new_node = Node(name, 0, self)  # Create a new node that will hold the data for directory
        self.directories[name] = new_node  # Add the directory to the current node
    def add_file(self, name, size):
        """
        Create method to add a file to the node
        """
        self.files[name] = size  # Add the file name and size to the files in this node
        current_node = self  # Set the current node to a variable called current node
        while current_node is not None:  # Continue next lines until the root node is reached
            current_node.size += size  # Add the file size to the size of this node
            current_node = current_node.parent  # Get the parent directory
    def get_directory(self, name):
        """
        Create a method to get a directory node
        """
        if name == '..':
            return self.parent  # Return the parent node if directory name is ..
        else:
            return self.directories[name]  # Return the node defined with the required name


def get_all_directories(pref, node):
    """
    Get all of the directories in a node
    Make sure to bring along the full path since some directory names are duplicated
    """
    values = dict()  # Create a dict to hold the data
    current_name = pref + node.name  # Get the name of the current node
    current_size = node.size  # Get the size of the current node
    values[current_name] = current_size  # Add these to the dict
    if len(node.directories) > 0:  # Check if there are directories under the current one.
        temp = node.directories  # Get a dict of sub directories
        for _, next_node in temp.items():  # Loop through these sub directories
            # Recursive call to get directories from the sub directory
            add_these = get_all_directories(current_name + "/", next_node)
            for new_dir, new_size in add_these.items():  # Loop through these directories
                values[new_dir] = new_size  # Add these to the dict
    return values  # Return the directory dict


def print_tree(node, cnt):
    """
    This is a debug function to print out the file structure.
    """
    print("-"*cnt + node.name + " (dir) size: " + str(node.size))  # print the current directory
    dirs = node.directories  # Get the sub directories
    files = node.files  # Get the files in this directory
    if len(dirs) > 0:  # Use only if there are sub directories
        for _, node in dirs.items():  # Loop through all sub directories
            print_tree(node, cnt + 1)  # Recursive call to print tree of sub directories
    if len(files) > 0:  # Use only if there are files present
        for name, size in files.items():  # Loop through all files
            print("-"*(cnt + 1) + name + " (file) size: " + str(size))  # print the file information


with open("puzzle_input.txt") as f:  # Open input file
    for line in f:  # Get a line of the file
        line = line.split()  # Split the line on spaces
        if line[0] == '$':  # This line is a command  ls is ignored.
            if line[1] == 'cd':  # This command is changing the directory
                name = line[2]  # Get the name of the new directory
                if name == '/':  # This is the root directory
                    root = Node('/', 0, None)  # Create a new file structure
                    current_node = root  # Set root as the current node 
                else:  # otherwise get the node of the requested directory
                    current_node = current_node.get_directory(name)
        elif line[0] == 'dir':  # This line defines a new directory
            name = line[1]  # Name of the new directory
            current_node.add_directory(name)  # Add this new directory to the current node
        else:  # This is a file name
            name = line[1]  # Get the file name
            size = int(line[0])  # Get the size of the file
            current_node.add_file(name, size)  # Add this file to the current directory


# Get the directories and their sizes
all_dirs = get_all_directories("", root)

# Find the sum of the directories with at most 100000 as a size
COUNT = 0
for _, size in all_dirs.items():
    if size <= 100000:
        COUNT += size

# Print the output
print(f"The sum is: {COUNT}.")
