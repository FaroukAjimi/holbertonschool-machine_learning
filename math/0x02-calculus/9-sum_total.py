#!/usr/bin/env python3
def summation_i_squared(n):
    t = type(1)
    if type(n) is not t:
        return(None)
    lis = [*range(1, n + 1)]
    po = list(map(lambda x: x ** 2, lis))
    return (sum(po))
