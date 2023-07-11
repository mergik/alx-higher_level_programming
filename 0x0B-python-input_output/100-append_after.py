#!/usr/bin/python3
"""Module that contains the function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing
    a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after the lines
        containing the search string.

    Returns:
        None
    """
    with open(filename, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
