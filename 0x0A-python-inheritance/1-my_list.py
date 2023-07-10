#!/usr/bin/python3
"""
A module that inherits the built-in list class and prints it in sorted order
"""


class MyList(list):
    """
    A custom list class that inherits the built-in list class.

    This class provides an additional method `print_sorted()`
    that prints the list, but in sorted (ascending) order.
    """

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)
