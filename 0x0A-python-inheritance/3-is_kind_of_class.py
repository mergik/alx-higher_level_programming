#!/usr/bin/python3
"""
Module that returns a boolean if the object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the given object is an instance of, or if the object is an
    instance of a class that inherited frm, the specified class.

    Parameters:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of, or if the object is an
        instance of a class that inherited frm, the specified class;
        False otherwise.
    """
    return isinstance(obj, a_class)
