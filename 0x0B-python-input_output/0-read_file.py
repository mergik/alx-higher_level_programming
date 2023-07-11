#!/usr/bin/python3
"""Module containing the function read_file"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read (optional).

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents)
