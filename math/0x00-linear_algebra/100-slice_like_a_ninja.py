#!/usr/bin/env python3
"""slicing like a ninja"""


def np_slice(matrix, axes={}):
    """slice function
    @matrix: matrix to slice
    @axes: axes"""
    lis = []
    for i in range(len(matrix.shape)):
        t = slice(*axes.get(i, (None, None)))
        lis.append(t)
    return(matrix[tuple(lis)])
