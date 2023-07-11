#!/usr/bin/python3
"""
Geometry related modules
"""


class BaseGeometry:
    """
    A base class for geometry-related classes.

    This class provides a foundation for implementing
    geometry-specific functionality.
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to be an integer greater than 0.

        Parameters:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
