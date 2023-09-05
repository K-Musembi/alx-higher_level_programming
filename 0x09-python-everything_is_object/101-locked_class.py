#!/usr/bin/python3
'''A module that defines a class'''


class LockedClass:
    '''A locked class'''

    __slots__ = ['first_name']

    def __init__(self, first_name=None):
        '''Initialize objects'''

        self.first_name = first_name
