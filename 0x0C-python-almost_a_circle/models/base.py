#!/usr/bin/python3
"""
This module contains the Base class that is used by other classes
to manage 'id' attribute
"""
import json
import csv
import turtle


class Base:
    """
    This is the base class for all other classes in the project.
    It manages the 'id' attribute and avoids duplicating code.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.
        """
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs]
        )
        with open(filename, 'w') as file:
            file.write(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize the instances to CSV format and write them to a file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances based on a JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                data = cls.from_json_string(json_data)
                instances = [cls.create(**item) for item in data]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize instances from a CSV file and return a list of instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    instances.append(cls.create_from_csv_row(row))
                return instances
        except FileNotFoundError:
            return []

    def to_csv_row(self):
        """
        Return list representing the instance attributes for CSV serialization
        """
        raise NotImplementedError(
            "to_csv_row method must be implemented in the child class"
        )

    @classmethod
    def create_from_csv_row(cls, row):
        """
        Create an instance from a CSV row.
        """
        raise NotImplementedError(
            "create_from_csv_row method must be implemented in the child class"
        )

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw all the rectangles and squares using the Turtle graphics module.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.

        Returns:
            None
        """
        screen = turtle.Screen()
        screen.bgcolor("white")

        pen = turtle.Turtle()
        pen.speed(0)

        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.color("red")
            for _ in range(2):
                pen.forward(rectangle.width)
                pen.right(90)
                pen.forward(rectangle.height)
                pen.right(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("blue")
            for _ in range(4):
                pen.forward(square.size)
                pen.right(90)

        turtle.done()
