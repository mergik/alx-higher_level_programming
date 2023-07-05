#!/usr/bin/python3

"""
This module contains the LockedClass that restricts the creation of new
instance attributes, except for the attribute named 'first_name'.
"""


class LockedClass:
    """
    LockedClass restricts the creation of new instance attributes,
    except for 'first_name'.
    """

    __slots__ = ['first_name']

    def __setattr__(self, attr, value):
        """
        Overrides setattr method to control creation of instance attributes.

        Args:
            attr (str): The attribute name being set.
            value (Any): The value to be assigned to the attribute.

        Raises:
            AttributeError: If the attribute is not 'first_name'.
        """
        if attr != 'first_name':
            raise AttributeError(
                f"'LockedClass' object has no attribute '{attr}'"
            )
        object.__setattr__(self, attr, value)
