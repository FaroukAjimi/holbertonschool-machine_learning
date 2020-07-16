#!/usr/bin/env python3
"""task 2"""


def matrix_shape(matrix):
    """amatrix shape"""
    a = []
    c = []
    t = type(a)
    while True:
        if type(matrix) is t:
            c.append(len(matrix))
            matrix = matrix[0]
        else:
            break
    return(c)
