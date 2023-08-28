#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print('{:d}'.format(my_list[i]), end="")
            elif type(my_list[i]) == str:
                print(my_list[i], end="")
            elif type(my_list[i]) == float:
                print('{:f}'.format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass
    print()

    return count
