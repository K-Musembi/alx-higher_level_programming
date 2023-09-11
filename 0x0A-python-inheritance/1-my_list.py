#!/usr/bin/python3
'''Defines a class'''


class MyList(list):
    '''Inherits from a list'''

    def print_sorted(self):
        '''List in sorted order'''

        self.sort()
        print(self)
