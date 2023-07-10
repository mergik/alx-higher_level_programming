#!/usr/bin/python3
"""
Module that returns a boolean if the object is/n't an instance of the
specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if the given object is exactly an instance of the specified class.

    Parameters:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified
        class; False otherwise.
    """
    return type(obj) is a_class
