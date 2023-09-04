#!/usr/bin/python3
'''Contains a printing function'''


def text_indentation(text):
    '''Prints two new lines'''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        if char == '.' or char == '?' or char == ':':
            line += char
            print(line.strip())
            print()
            line = ""
            continue
        line += char
    print(line.strip(), end="")
