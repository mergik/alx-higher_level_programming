#!/usr/bin/python3
"""This module contains the Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a square and inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object.

        Args:
            size (int): The size of the square (width and height).
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The ID of the square (optional).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
