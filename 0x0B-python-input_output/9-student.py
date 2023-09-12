#!/usr/bin/python3
'''Defines a class'''


class Student:
    '''A student class'''

    def __init__(self, first_name, last_name, age):
        '''Initialize an object'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Dictionary representation  of instance'''

        return self.__dict__
