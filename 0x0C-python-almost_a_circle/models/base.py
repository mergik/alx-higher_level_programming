#!/usr/bin/python3
"""
This module contains the Base class that is used by other classes
to manage 'id' attribute
"""


class Base:
    """
    This is the base class for all other classes in the project.
    It manages the 'id' attribute and avoids duplicating code.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int): The ID of the object (optional).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
