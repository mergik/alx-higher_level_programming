import unittest
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):

    def test_init(self):
        # Test initializing a Rectangle object
        rect = Rectangle(5, 10, 1, 2, 3)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 3)

    def test_width(self):
        # Test getter and setter for width attribute
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        rect.width = 7
        self.assertEqual(rect.width, 7)

    def test_height(self):
        # Test getter and setter for height attribute
        rect = Rectangle(5, 10)
        self.assertEqual(rect.height, 10)
        rect.height = 12
        self.assertEqual(rect.height, 12)

    def test_x(self):
        # Test getter and setter for x attribute
        rect = Rectangle(5, 10, 1, 2)
        self.assertEqual(rect.x, 1)
        rect.x = 3
        self.assertEqual(rect.x, 3)

    def test_y(self):
        # Test getter and setter for y attribute
        rect = Rectangle(5, 10, 1, 2)
        self.assertEqual(rect.y, 2)
        rect.y = 4
        self.assertEqual(rect.y, 4)


if __name__ == '__main__':
    unittest.main()
