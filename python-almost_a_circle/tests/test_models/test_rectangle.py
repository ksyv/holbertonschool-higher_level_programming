#!/usr/bin/python3

"""define unittests for rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class testRectangleCreation(unittest.TestCase):
    """Tests for check if rectangle instance is created with good arg,
    and Base inheritance"""
    def testInheritance(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def testWithoutArgs(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def testOneArg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def testMoreFiveArgs(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def testWithNoIntArg(self):
        with self.assertRaises(TypeError):
            rectangle1 = Rectangle("Str", 2)
        with self.assertRaises(TypeError):
            rectangle1 = Rectangle(2, "Str")
        with self.assertRaises(TypeError):
            rectangle1 = Rectangle(2, 10, 'Str', 5)
        with self.assertRaises(TypeError):
            rectangle1 = Rectangle(23, 12, 4, 'Str')

    def testWithZeroValue(self):
        with self.assertRaises(ValueError):
            rectangle1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            rectangle1 = Rectangle(2, 0)

    def testWithNegativeValue(self):
        with self.assertRaises(ValueError):
            rectangle1 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            rectangle1 = Rectangle(2, -1)
        with self.assertRaises(ValueError):
            rectangle1 = Rectangle(2, 10, -1, 5)
        with self.assertRaises(ValueError):
            rectangle1 = Rectangle(23, 12, 4, -1)


class TestRectangleIdIdentation(unittest.TestCase):
    """Tests for check the id attribution of all instance"""
    def testWithoutIDArg(self):
        rectangle1 = Rectangle(10, 2)
        rectangle2 = Rectangle(2, 10, 4, 5)
        self.assertEqual(rectangle1.id, rectangle2.id - 1)

    def testIdGive(self):
        rectangle1 = Rectangle(10, 2, 4, 5, 7)
        self.assertEqual(rectangle1.id, 7)

    def testIdManualyAssignment(self):
        rectangle1 = Rectangle(10, 2, 4, 5, 7)
        rectangle1.id = 13
        self.assertEqual(rectangle1.id, 13)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)




if __name__ == "__main__":
    unittest.main()
