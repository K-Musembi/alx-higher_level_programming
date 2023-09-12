#!/usr/bin/python3
'''Defines a class'''


class Student:
    '''A student class'''

    def __init__(self, first_name, last_name, age):
        '''Initialize an object'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Dictionary representation  of instance'''

        if type(attrs) == list and isinstance(attrs[0], str):
            (print(i.__dict__) for i in attrs)

        return self.__dict__
