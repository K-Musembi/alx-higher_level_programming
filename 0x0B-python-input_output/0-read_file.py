#!/usr/bin/python3
'''Defines a function'''


def read_file(filename=""):
    '''Read file and print'''

    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
