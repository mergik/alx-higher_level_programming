#!/usr/bin/python3
"""
This module provides a function for printing the name in a specific format.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name (optional). Defaults to an empty string

    Raises:
        TypeError: If `first_name` is not a string or `last_name`
        is not a string.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
