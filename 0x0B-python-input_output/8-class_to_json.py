#!/usr/bin/python3
"""Module containing the function class_to_json"""


def class_to_json(obj):
    """
    Returns a dictionary representation of an object with
    simple data structures for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representation of the object.
    """
    if not hasattr(obj, "__dict__"):
        return obj

    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
        elif isinstance(value, type(None)):
            result[key] = None
        else:
            result[key] = class_to_json(value)
    return result
