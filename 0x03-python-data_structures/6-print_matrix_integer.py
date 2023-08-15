#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        flag = -1
        for column in row:
            flag += 1
            if flag == len(row) - 1:
                print('{:d}'.format(column), end='')
            else:
                print('{:d}'.format(column), end=' ')
        print()
