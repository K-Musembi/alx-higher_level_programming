#!/usr/bin/python3
'''Function to append text file'''


def append_write(filename="", text=""):
    '''Append text file'''

    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
