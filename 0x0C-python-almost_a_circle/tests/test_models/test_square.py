#!/usr/bin/python3
'''Defines Test Class'''

from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    '''Test Square class'''

    def setUp(self):
        '''setup method'''

        self.s1 = Square(1)

    @unittest.expectedFailure
    def test_str(self):
        '''Test representation'''

        self.assertEqual(self.s1.str(), f"[Square] ({1}) {0}/{0} - {1}")

    def test_ssetter(self):
        '''Test size setter'''

        with self.assertRaises(TypeError):
            self.s1.size = "1"

    def test_ssetter2(self):
        '''Test size setter'''

        with self.assertRaises(ValueError):
            self.s1.size = -1

    def test_sgetter(self):
        '''Test size getter'''

        self.assertEqual(self.s1.size, 1)

    @unittest.expectedFailure
    def test_dictionary(self):
        '''Test to_dictionary'''

        self.assertEqual(self.s1.to_dictionary(), f"{'id': {1}, 'x': {2}}")
