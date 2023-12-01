#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""Unittest Case for 6-max_integer module
"""

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """Testing the function with integer list contents
        """
        self.assertEqual(max_integer([1, 4, 7]), 7)
        self.assertEqual(max_integer([-2, -4, -7]), -2)
        self.assertEqual(max_integer([0]), 0)

    def tes_max_integer(self):
        """Testing with empty list passed as argument
        """
        self.assertEqual(max_integer([]), None)

    def test_max_integer_raises(self):
        """Testing the function with different data types passed as arguments
        """
        self.assertRaises(TypeError, max_integer, dict)
        self.assertRaises(TypeError, max_integer, tuple)
        self.assertRaises(TypeError, max_integer, set)
        self.assertRaises(TypeError, max_integer, str)
        self.assertRaises(TypeError, max_integer, bool)

    def test_max_integer(self):
        """Testing with list containing different data type
        """
        mixed = ["1", 77, True]
        with self.assertRaises(TypeError):
            max_integer(mixed)

    def test_max_integer_duplicate(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_max_integer_large_list(self):
        """Testing the function with large list
        """
        self.assertEqual(max_integer([x for x in range(10000)]), 9999)

if __name__ == '__main__':
    unittest.main()
