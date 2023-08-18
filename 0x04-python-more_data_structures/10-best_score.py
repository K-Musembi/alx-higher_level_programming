#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary:
        largest = max(a_dictionary, key = lambda i: a_dictionary[i])
    else:
        return

    return largest
