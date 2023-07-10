#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
        obj: Any object - The object for which to retrieve the attributes
        and methods.

    Returns:
        list: A list containing the names of available attributes
        and methods of the object.
    """
    attributes = []
    methods = []

    # Get all attributes and methods of the object
    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)
        if callable(attr_value):
            methods.append(attr_name)
        else:
            attributes.append(attr_name)

    # Return the list of attributes and methods
    return attributes + methods
