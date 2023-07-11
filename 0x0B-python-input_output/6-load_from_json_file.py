#!/usr/bin/python3
"""Module containing the function save_to_json_file"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The object created from the JSON file.
    """
    with open(filename, "r") as file:
        return json.load(file)
