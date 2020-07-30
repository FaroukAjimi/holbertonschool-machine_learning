#!/usr/bin/env python3
def summation_i_squared(n):
    try:
        lis = [*range(1, n + 1)]
    except:
        return(None)
    po = list(map(lambda x: x ** 2, lis))
    return (sum(po))
