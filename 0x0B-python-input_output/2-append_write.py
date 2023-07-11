#!/usr/bin/python3
"""Module containing the function append_write"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF-8 text file and returns the number of
    characters added.

    Args:
        filename (str): The name of the file to append (optional).
        text (str): The string to append to the file (optional).

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
