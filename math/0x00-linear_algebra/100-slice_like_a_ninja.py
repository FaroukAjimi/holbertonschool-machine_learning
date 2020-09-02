#!/usr/bin/env python3
import numpy as np

def np_slice(matrix, axes={}):
    lis = []
    for i in range(len(matrix.shape)):
        t = slice(*axes.get(i, (None, None)))
        lis.append(t)
    return(matrix[tuple(lis)])
    
