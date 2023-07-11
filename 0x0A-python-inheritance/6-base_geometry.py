#!/usr/bin/python3
"""
Geometry related modules
"""


class BaseGeometry:
    """
    A base class for geometry-related classes.

    This class provides a foundation for implementing geometry-specific
    functionality.
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
