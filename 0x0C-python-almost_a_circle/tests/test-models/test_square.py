import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(5)

    def test_attributes(self):
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square.height, 5)
        self.assertEqual(self.square.x, 0)
        self.assertEqual(self.square.y, 0)
        self.assertIsNone(self.square.id)

    def test_str(self):
        expected_str = "[Square] (None) 0/0 - 5"
        self.assertEqual(str(self.square), expected_str)

    def test_size_setter(self):
        self.square.size = 10
        self.assertEqual(self.square.size, 10)
        self.assertEqual(self.square.width, 10)
        self.assertEqual(self.square.height, 10)

    def test_to_dictionary(self):
        expected_dict = {
            'id': None,
            'size': 5,
            'x': 0,
            'y': 0
        }
        self.assertEqual(self.square.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
