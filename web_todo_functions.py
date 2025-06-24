FILEPATH = "todos.txt"  # Global variable for the file path
import os
import sys

def get_todos(filepath=FILEPATH):# Default value for filepath
    """Read the text file and return the list of todos."""
    with open(filepath, "r") as file_local: # local variable file_local
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH): # allways put non-default arguments first
    """Write the list of todos to the text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)