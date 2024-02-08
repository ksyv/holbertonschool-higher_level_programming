import unittest
max_integer = __import__('6-max_integer').max_integer


class test_max_integer(unittest.TestCase):
    """class for testing max_integer function"""
    def testempty(self):
        # test if list is empty
        empty = []
        self.assertEqual(max_integer(empty), None)

    def testvraclist(self):
        # test a lambda list
        vrac = [4, 6, 2, 5]
        self.assertEqual(max_integer(vrac), 6)

    def maxatbegging(self):
        # test if the max is the first listed number
        beggining = [6, 2, 4, 3]
        self.assertEqual(max_integer(beggining), 6)

    def withnegatif(self):
        # test with a list of negativ number
        withnegatif = [-6, -9, -2, -3]
        self.assertEqual(max_integer(withnegatif), -2)

    def negatifAndPositif(self):
        # test with negatif and positif number
        posAndNeg = [4, -6, 18, -23]
        self.assertEqual(max_integer(posAndNeg), 18)

    def only(self):
        # test if list contain only one number
        only = [5]
        self.assertEqual(max_integer(only), 5)
    
    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)
