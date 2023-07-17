import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):

    def test_init_with_id(self):
        # Test initializing with a specified ID
        obj = Base(id=1)
        self.assertEqual(obj.id, 1)

    def test_init_without_id(self):
        # Test initializing without a specified ID
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_init_with_negative_id(self):
        # Test initializing with a negative ID
        obj = Base(id=-1)
        self.assertEqual(obj.id, -1)

    def test_init_with_zero_id(self):
        # Test initializing with an ID of zero
        obj = Base(id=0)
        self.assertEqual(obj.id, 0)


if __name__ == '__main__':
    unittest.main()
