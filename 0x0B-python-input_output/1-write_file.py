#!/usr/bin/python3
'''Fuction to write to file'''


def write_file(filename="", text=""):
    '''Write to file'''

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
