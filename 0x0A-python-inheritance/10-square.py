#!/usr/bin/python3
"""
Geometry related modules
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    This class inherits from the Rectangle class and provides
    functionality specific to squares.
    """

    def __init__(self, size):
        """
        Initializes a square with the specified size.

        Parameters:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
