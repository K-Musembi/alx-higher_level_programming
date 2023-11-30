#!/usr/bin/python3
""" Find peak element
"""


def find_peak(list_of_integers):
    """ Find the peak """

    length = len(list_of_integers)

    if length == 0:
        return None
    elif length == 1:
        return list_of_integers[0]
    elif length == 2:
        if list_of_intgers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]
    else:
        for item in range(1, length):
            if list_of_integers[item] > list_of_integers[item - 1]\
                    and list_of_integers[item] > list_of_integers[item + 1]:
                return list_of_integers[item]
        else:
            if list_of_integers[0] >= list_of_integers[length - 1]:
                return list_of_integers[0]
            else:
                return list_of_integers[length - 1]
