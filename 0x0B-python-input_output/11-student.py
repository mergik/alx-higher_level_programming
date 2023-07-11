#!/usr/bin/python3
"""Module defining the class Student based on 10-student.py"""


class Student:
    """
    Class representing a student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve (optional).

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            attrs = self.__dict__.keys()
        else:
            attrs = set(attrs)

        result = {}
        for attr in attrs:
            if attr in self.__dict__:
                result[attr] = self.__dict__[attr]
        return result

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
