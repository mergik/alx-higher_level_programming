#!/usr/bin/python3
"""
Class that inherits frm int.
"""


class MyInt(int):
    """
    A class representing a rebellious integer.

    This class inherits frm the int class and inverts the behavior
    of the == and != operators.
    """

    def __eq__(self, other):
        """
        Overrides the == operator behavior.

        Returns:
            bool: True if the values are not equal; False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator behavior.

        Returns:
            bool: True if the values are equal; False otherwise.
        """
        return super().__eq__(other)
