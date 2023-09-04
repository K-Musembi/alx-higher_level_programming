#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Tests for max_integer([..])'''

    def test_input(self):
        '''Test function input'''

        self.assertEqual(max_integer([1, 5, 3, 2]), 5)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -1]), -1)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1.2, 2.3]), 2.3)

        @unittest.expectedFailure
        def test_type(self):
            '''Test object type'''

            self.assertRaises(TypeError, max_integer, 'hello')
            self.assertRaises(TypeError, max_integer, {1 : 'one'})
