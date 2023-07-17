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
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
