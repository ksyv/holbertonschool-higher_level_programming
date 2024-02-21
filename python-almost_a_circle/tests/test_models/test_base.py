#!/usr/bin/python3

"""define unittests for base.py"""
import unittest
import json
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

    def setUp(self):
        """
        Function to set up a new instance
        """
        self.base = Base()
        
    def test_to_json_string1(self):
        """
        Tests if to_json_string function
        correctly convert an instance to a json string
        """
        result = self.base.to_json_string({"id": 1, "man": "Oboy"})
        self.assertEqual(result, '{"id": 1, "man": "Oboy"}')

    def test_to_json_string2(self):
        """
        Tests if to_json_string function
        correctly convert an instance to a json string
        """
        self.assertEqual(self.base.to_json_string([]), '[]')

    def test_to_json_string3(self):
        """
        Tests if to_json_string function
        correctly convert an instance to a json string
        """
        self.assertEqual(self.base.to_json_string(None), '[]')

    def test_json_save_empty(self):
        """
        Tests function if an empty paramter is passed
        """
        with self.assertRaises(TypeError) as e:
            self.base.save_to_file()

    def test_json_load1(self):
        """
        Tests if functiond correctly deserialize a json string
        """
        result = self.base.from_json_string('[]')
        self.assertEqual(result, [])

    def test_json_load2(self):
        """
        Tests if functiond correctly deserialize a json string
        """
        self.assertEqual(self.base.from_json_string(None), [])

    def test_json_load3(self):
        """
        Tests if functiond correctly deserialize a json string
        """
        result = self.base.from_json_string('["hello", "world"]')
        self.assertEqual(result, ["hello", "world"])

    def test_json_load4(self):
        """
        Tests if functiond correctly deserialize a json string
        """
        with self.assertRaises(json.decoder.JSONDecodeError):
            self.base.from_json_string("Wrong input")

    def test_json_load5(self):
        """
        Tests if functiond correctly deserialize a json string
        """
        result = self.base.from_json_string('{"id": 1, "m" : "hey"}')
        self.assertEqual(result, {"id": 1, "m": "hey"})


if __name__ == "__main__":
    unittest.main()
