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
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle1 = Rectangle("Str", 2)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            rectangle1 = Rectangle(2, "Str")
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rectangle1 = Rectangle(2, 10, 'Str', 5)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            rectangle1 = Rectangle(23, 12, 4, 'Str')

    def testWithZeroValue(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle1 = Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle1 = Rectangle(2, 0)

    def testWithNegativeValue(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle1 = Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle1 = Rectangle(2, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rectangle1 = Rectangle(2, 10, -1, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
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


class TestRectangleArea(unittest.TestCase):
    """Tests the area method"""
    def testArea(self):
        rectangle1 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, rectangle1.area())

    def testAreaWithArg(self):
        rectangle1 = Rectangle(10, 2, 0, 0, 0)
        with self.assertRaises(TypeError):
            rectangle1.area(1)


if __name__ == "__main__":
    unittest.main()
