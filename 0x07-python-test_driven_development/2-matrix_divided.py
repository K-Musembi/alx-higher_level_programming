#!/usr/bin/python3
'''A module that contains a function'''


def matrix_divided(matrix, div):
    '''A function that divides a matrix'''

    new_matrix = []

    num = [[isinstance(i, int) or isinstance(i, float)
            for i in list] for list in matrix]
    for list in num:
        if not all(list):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")

    size = len(matrix[0])
    length = [size == len(row) for row in matrix]
    if not all(length):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(i / div, 2) for i in list] for list in matrix]

    return new_matrix
