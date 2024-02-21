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

if __name__ == "__main__":
    unittest.main()