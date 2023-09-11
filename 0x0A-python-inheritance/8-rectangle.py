#!/usr/bin/python3
'''Base class and child class'''


class BaseGeometry:
    '''A geometry class'''

    def area(self):
        '''An empty function'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''A validation method'''

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    '''A rectangle class'''

    def __init__(self, width, height):
        '''Initializes an object'''

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
