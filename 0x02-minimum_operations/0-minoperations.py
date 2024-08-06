#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ .... """
    op = 0
    h = z = 1

    while n > h:
        if n % h == 0:
            z = h
            h += h
            op += 2
        else:
            h += z
            op += 1

    return op
