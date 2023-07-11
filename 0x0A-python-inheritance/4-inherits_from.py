#!/usr/bin/python3
"""
Module that returns boolean if an object is an instance of a class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the given object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Parameters:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class;
              False otherwise.
    """

    return issubclass(type(obj), a_class)
