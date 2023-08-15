#!/usr/bin/python3

def max_integer(my_list=[]):

    largest = 0
    if len(my_list) == 0:
        return
    elif len(my_list) == 1:
        largest = my_list[0]
    else:
        for num in my_list:
            if num > largest:
                largest = num

    return largest
