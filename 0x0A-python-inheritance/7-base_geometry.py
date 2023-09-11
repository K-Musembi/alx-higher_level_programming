#!/usr/bin/python3
'''Defines a class'''


class BaseGeometry:
    '''An geometry class'''

    def area(self):
        '''An empty function'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''A validation method'''

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
