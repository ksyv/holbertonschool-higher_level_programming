#!/usr/bin/python3

"""define unittests for base.py"""
import unittest
from models.base import Base


class TestIdIdentation(unittest.TestCase):
    """Tests for check the id attribution of all instance"""
    def testIdWithoutArg(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def testIdIsNone(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def testIdWithoutArg3instance(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base2.id - 1, base3.id - 2)

    def testIdGive(self):
        base1 = Base(12)
        self.assertEqual(base1.id, 12)

    def testIdWithoutArgBetwinOneGive(self):
        base1 = Base()
        base2 = Base(12)
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 1)

    def testIdManualyAssignment(self):
        base1 = Base(12)
        base1.id = 13
        self.assertEqual(base1.id, 13)

    def testTwoArgs(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == "__main__":
    unittest.main()
