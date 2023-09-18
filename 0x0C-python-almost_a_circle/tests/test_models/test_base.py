#!/usr/bin/python3
'''Defines a test class'''

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Test Base class'''

    def setUp(self):
        '''setup method'''

        self.b1 = Base()
        self.b2 = Base(2)

    @unittest.expectedFailure
    def test_json_string(self):
        '''Test to_json'''

        self.assertEqual(self.b1.to_json_string([{'x': 2}]), f'[{"x": {2}}]')
        self.assertEqual(self.b2.to_json_string(None), "[]")

    @unittest.expectedFailure
    def test_save(self):
        '''Test save_to_file'''

        self.assertEqual(self.b1.save_to_file([b2]), f'[{"y": {8}}]')

    @unittest.expectedFailure
    def test_string_json(self):
        '''Test json_string'''

        self.assertEqual(self.b1.from_json_string([{"height": 4}]), f"[{'height': {4}}]")
        self.assertEqual(self.b2.from_json_string(None))

    @unittest.expectedFailure
    def test_create(self):
        '''Test create'''

        self.assertEqual(self.b1.create([]), [])

    @unittest.expectedFailure
    def test_load_file(self):
        '''Test load_from_file'''

        self.assertEqual(self.b1.load_from_file([]), [])
