#!/usr/bin/python3
"""
Function that add new attribute to an object if possible.
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to the object if it's possible.

    Parameters:
        obj (object): The object to add the attribute to.
        attr_name (str): The name of the attribute.
        attr_value: The value of the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if hasattr(obj, "__dict__"):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("can't add new attribute")
