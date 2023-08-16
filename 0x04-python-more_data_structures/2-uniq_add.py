#!/usr/bin/python3

def uniq_add(my_list=[]):

    result = 0
    flag = []

    for num in my_list:
        if num in flag:
            continue
        else:
            result += num
            flag.append(num)

    return result
