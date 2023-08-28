#!/usr/bin/python3

from sys import stderr


def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
    except Exception as exc:
        print("Exception:", exc, file=stderr)
        return False

    return True
