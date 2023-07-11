#!/usr/bin/python3
"""Module containing the function write_file"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 text file and returns the number of characters written.

    Args:
        filename (str): The name of the file to write (optional).
        text (str): The string to write to the file (optional).

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
