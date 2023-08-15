#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tuple1 = tuple_a[:2] + (0, 0)
    tuple2 = tuple_b[:2] + (0, 0)
    one = tuple1[0] + tuple2[0]
    two = tuple1[1] + tuple2[1]

    new_tuple = (one, two)
    return new_tuple
