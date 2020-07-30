#!/usr/bin/env python3
# SIgma alogrithm


def summation_i_squared(n):
    """ function sum_i_squared
    from i = 1
    to i = n
    while i is squared """
    t = type(1)
    if type(n) is not t:
        return(None)
    lis = [*range(1, n + 1)]
    po = list(map(lambda x: x ** 2, lis))
    return (sum(po))
