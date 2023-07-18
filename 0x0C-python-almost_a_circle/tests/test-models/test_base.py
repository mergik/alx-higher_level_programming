import unittest
from unittest.mock import patch
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        self.obj1 = Base()
        self.obj2 = Base()
        self.obj3 = Base(10)

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_init_without_id(self):
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj2.id, 2)
        self.assertEqual(self.obj3.id, 10)

    def test_init_with_id(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_create_rectangle(self):
        with patch('base.Rectangle') as mock_rect:
            mock_rect.return_value = 'Rectangle'
            obj = Base.create(type='Rectangle')
            self.assertEqual(obj, 'Rectangle')

    def test_create_square(self):
        with patch('base.Square') as mock_square:
            mock_square.return_value = 'Square'
            obj = Base.create(type='Square')
            self.assertEqual(obj, 'Square')

    def test_create_invalid_type(self):
        obj = Base.create(type='Invalid')
        self.assertIsNone(obj)

    def test_to_json_string(self):
        obj1 = {'id': 1, 'width': 10, 'height': 5}
        obj2 = {'id': 2, 'size': 3}
        obj_list = [obj1, obj2]
        expected_json = '[{"id": 1, "width": 10, "height": 5}, {"id": 2, "size": 3}]'
        json_string = Base.to_json_string(obj_list)
        self.assertEqual(json_string, expected_json)

    def test_from_json_string(self):
        json_string = '[{"id": 1, "width": 10, "height": 5}, {"id": 2, "size": 3}]'
        expected_list = [{'id': 1, 'width': 10, 'height': 5}, {'id': 2, 'size': 3}]
        obj_list = Base.from_json_string(json_string)
        self.assertEqual(obj_list, expected_list)

    def test_save_to_file(self):
        with patch('builtins.open', create=True) as mock_file:
            mock_write = mock_file.return_value.__enter__.return_value.write
            Base.save_to_file([self.obj1, self.obj2])
            mock_write.assert_called_once()

    def test_save_to_file_csv(self):
        with patch('builtins.open', create=True) as mock_file:
            mock_write = mock_file.return_value.__enter__.return_value.write
            self.obj1.to_csv_row = lambda: [1, 10, 5]
            self.obj2.to_csv_row = lambda: [2, 3]
            Base.save_to_file_csv([self.obj1, self.obj2])
            mock_write.assert_called_once()

    def test_load_from_file(self):
        with patch('builtins.open', create=True) as mock_file:
            mock_read = mock_file.return_value.__enter__.return_value.read
            mock_read.return_value = '[{"id": 1, "width": 10, "height": 5}, {"id": 2, "size": 3}]'
            obj_list = Base.load_from_file()
            self.assertEqual(len(obj_list), 2)

    def test_load_from_file_csv(self):
        with patch('builtins.open', create=True) as mock_file:
            mock_read = mock_file.return_value.__enter__.return_value.read
            mock_read.return_value = '1,10,5\n2,3\n'
            obj_list = Base.load_from_file_csv()
            self.assertEqual(len(obj_list), 2)

    def test_to_csv_row(self):
        with self.assertRaises(NotImplementedError):
            self.obj1.to_csv_row()

    def test_create_from_csv_row(self):
        with self.assertRaises(NotImplementedError):
            Base.create_from_csv_row([])

    @patch('turtle.Screen')
    @patch('turtle.Turtle')
    def test_draw(self, mock_turtle, mock_screen):
        mock_pen = mock_turtle.return_value
        obj1 = type('Rectangle', (), {'x': 0, 'y': 0, 'width': 10, 'height': 5})
        obj2 = type('Square', (), {'x': 20, 'y': 20, 'size': 3})
        list_rectangles = [obj1]
        list_squares = [obj2]
        Base.draw(list_rectangles, list_squares)
        mock_screen.assert_called_once()
        mock_pen.penup.assert_called_with()
        mock_pen.goto.assert_called_with(0, 0)
        mock_pen.pendown.assert_called_with()
        mock_pen.forward.assert_called_with(10)
        mock_pen.right.assert_called_with(90)
        mock_pen.forward.assert_called_with(5)
        mock_pen.right.assert_called_with(90)
        mock_pen.penup.assert_called_with()
        mock_pen.goto.assert_called_with(20, 20)
        mock_pen.pendown.assert_called_with()
        mock_pen.forward.assert_called_with(3)
        mock_pen.right.assert_called_with(90)


if __name__ == '__main__':
    unittest.main()
