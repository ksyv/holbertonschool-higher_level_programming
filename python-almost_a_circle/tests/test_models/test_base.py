#!/usr/bin/python3

"""define unittests for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

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


class TestJsonTraitment(unittest.TestCase):
    """test json methods of class Base"""
    def testToJsonStringRectangle(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def testToJsonStringRectangleTwoDicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)
    def testToJsonStringList(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def testToJsonStringNone(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def testToJsonStringWithoutArgs(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def testToJsonStringMoreThanOneArg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def testFromJsonStringOneRectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def testFromJsonStringTwoRectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def testFromJsonStringNone(self):
        self.assertEqual([], Base.from_json_string(None))

    def testFromJsonStringEmptyList(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def testFromJsonStringNoArgs(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def testFromJsonStringMoreThanOneArg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


if __name__ == "__main__":
    unittest.main()
