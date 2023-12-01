#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""Unittest Case for 6-max_integer module
"""

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 4, 7]), 7)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-2, -4, -7]), -2)
        self.assertEqual(max_integer([0]), 0)
        self.assertRaises(TypeError, max_integer, dict)
        self.assertRaises(TypeError, max_integer, tuple)
        self.assertRaises(TypeError, max_integer, set)
        self.assertRaises(TypeError, max_integer, str)
        self.assertRaises(TypeError, max_integer, bool)
        self.assertRaises(TypeError, max_integer, [1, "2"])

if __name__ == '__main__':
    unittest.main()
