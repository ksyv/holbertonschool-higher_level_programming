#!/usr/bin/python3

"""define unittests for square.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testSquareCreation(unittest.TestCase):
    """Tests for check if square instance is created with good arg,
    and Base inheritance"""
    def testInheritance(self):
        self.assertIsInstance(Square(10), Base)

    def testInheritanceOfRectangle(self):
        self.assertIsInstance(Square(10), Rectangle)

    def testWithoutArgs(self):
        with self.assertRaises(TypeError):
            Square()

    def testOneArg(self):
        Square(1)

    def testMoreFourArgs(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def testWithNoIntArg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square1 = Square("Str")
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            square1 = Square(2, 'Str', 5)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            square1 = Square(23, 12, 'Str')

    def testWithZeroValue(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square1 = Square(0)

    def testWithNegativeValue(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square1 = Square(-1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square1 = Square(2, -1, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square1 = Square(23, 12, -1)


class TestSquareIdIdentation(unittest.TestCase):
    """Tests for check the id attribution of all instance"""
    def testWithoutIDArg(self):
        square1 = Square(10)
        square2 = Square(2, 10, 4)
        self.assertEqual(square1.id, square2.id - 1)

    def testIdGive(self):
        square1 = Square(10, 2, 4, 7)
        self.assertEqual(square1.id, 7)

    def testIdManualyAssignment(self):
        square1 = Square(10, 2, 4, 7)
        square1.id = 13
        self.assertEqual(square1.id, 13)


class TestAssertAndSetterSquare(unittest.TestCase):
    """verify setter and assert"""
    def test_heightsetter(self):
        square = Square(12, 6, 0)
        square.size = 18
        self.assertEqual(square.size, 18)

    def test_heightsetterassert(self):
        self.assertRaises(ValueError, Square, -10, 6, 0, 0)

    def test_widthsetters(self):
        square = Square(12, 0, 0)
        square.size = 36
        self.assertEqual(square.size, 36)

    def test_widthsetterassert(self):
        self.assertRaises(ValueError, Square, 10, -6, 0, 0)

    def test_xsetters(self):
        square = Square(12, 6, 0, 0)
        square.x = 9
        self.assertEqual(square.x, 9)

    def test_xsetterassert(self):
        self.assertRaises(ValueError, Square, 6, -1, 0)

    def test_ysetters(self):
        square = Square(12, 6, 0, 0)
        square.y = 3
        self.assertEqual(square.y, 3)

    def test_ysetterassert(self):
        self.assertRaises(ValueError, Square, 6, 0, -1)


class TestSquareArea(unittest.TestCase):
    """Tests the area method"""
    def testArea(self):
        square1 = Square(10, 0, 0, 0)
        self.assertEqual(100, square1.area())

    def testAreaWithArg(self):
        square1 = Square(10, 0, 0, 0)
        with self.assertRaises(TypeError):
            square1.area(1)


class TestupdateSquare(unittest.TestCase):
    """test the update method"""
    def testUpdate(self):
        r1 = Square(10, 10, 10)
        r1.update(89, 2)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual([r1.id, r1.width, r1.height, r1.x, r1.y],
                         [89, 4, 2, 1, 3])


if __name__ == "__main__":
    unittest.main()
