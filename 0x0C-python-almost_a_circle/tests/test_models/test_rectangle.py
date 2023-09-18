#!/usr/bin/python3
'''Defines a test class'''

from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    '''Test Rectangle class'''

    def setUp(self):
        '''setup method'''

        self.r1 = Rectangle(1, 2)

    def test_wsetter(self):
        '''Test setter'''

        with self.assertRaises(TypeError):
            self.r1.width("1")

    @unittest.expectedFailure
    def test_hsetter(self):
        '''Test setter'''

        with self.assertRaises(ValueError):
            self.r1.height(-1)

    def test_wgetter(self):
        '''Test getter'''

        self.assertEqual(self.r1.width, 1)

    def test_hgetter(self):
        '''Test getter'''

        self.assertEqual(self.r1.height, 2)

    def test_area(self):
        '''Test area'''

        self.assertEqual(self.r1.area(), 2)

    @unittest.expectedFailure
    def test_display(self):
        '''Test display'''

        self.assertEqual(self.r1.display(), '##')

    @unittest.expectedFailure
    def test_str(self):
        '''Test representation'''

        self.assertEqual(self.r1.str(), f'[Rectangle] ({1}) {1}/{0} - {1}/{2}')

    @unittest.expectedFailure
    def test_update(self):
        '''Test update'''

        self.assertEqual(self.r1.update(89, 2, 10), f'[Rectangle] ({89}) {10}/{10} - {2}/{10}')

    @unittest.expectedFailure
    def test_dictionary(self):
        '''Test to_dictionary'''

        self.assertEqual(self.r1.to_dictionary(), f"{'x': {1}, 'y': {9}}")
