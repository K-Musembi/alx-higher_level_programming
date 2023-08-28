#!/usr/bin/python3

def safe_print_division(a, b):

    try:
        a / b
    except ZeroDivisionError:
        pass
    finally:
        if b == 0:
            print("Inside result: None")
            return
        else:
            print("Inside result: {}".format(a / b))
            return (a / b)
