import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        rect = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 100)

    def test_width(self):
        rect = Rectangle(5, 10)
        rect.width = 8
        self.assertEqual(rect.width, 8)

        with self.assertRaises(TypeError):
            rect.width = "not_an_integer"

        with self.assertRaises(ValueError):
            rect.width = -5

    def test_height(self):
        rect = Rectangle(5, 10)
        rect.height = 12
        self.assertEqual(rect.height, 12)

        with self.assertRaises(TypeError):
            rect.height = "not_an_integer"

        with self.assertRaises(ValueError):
            rect.height = -8

    def test_x(self):
        rect = Rectangle(5, 10)
        rect.x = 3
        self.assertEqual(rect.x, 3)

        with self.assertRaises(TypeError):
            rect.x = "not_an_integer"

        with self.assertRaises(ValueError):
            rect.x = -2

    def test_y(self):
        rect = Rectangle(5, 10)
        rect.y = 4
        self.assertEqual(rect.y, 4)

        with self.assertRaises(TypeError):
            rect.y = "not_an_integer"

        with self.assertRaises(ValueError):
            rect.y = -3

    def test_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        rect = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with patch('builtins.print') as mock_print:
            rect.display()
            mock_print.assert_called_with(expected_output)

    def test_str(self):
        rect = Rectangle(5, 10, 1, 2, 100)
        expected_output = "[Rectangle] (100) 1/2 - 5/10"
        self.assertEqual(str(rect), expected_output)

    def test_to_dictionary(self):
        rect = Rectangle(5, 10, 1, 2, 100)
        expected_dict = {
            'id': 100,
            'width': 5,
            'height': 10,
            'x': 1,
            'y': 2
        }
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_update(self):
        rect = Rectangle(5, 10, 1, 2, 100)
        rect.update(6, 12, 3, 4, 200)
        self.assertEqual(rect.width, 12)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 200)
        self.assertEqual(rect.id, 6)

        rect.update(width=8, height=15)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 15)


if __name__ == '__main__':
    unittest.main()
