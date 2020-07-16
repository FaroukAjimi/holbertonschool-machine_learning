#!/usr/bin/env python3
"""copet"""
import copy
def cat_matrices2D(mat1, mat2, axis=0):
    """ cat mat"""
    new = []
    lis1 = []
    a = copy.deepcopy(mat1)
    b = copy.deepcopy(mat2)
    try:
        if axis == 0:
            for i in range(len(a)):
                new.append(a[i])
            for i in range(len(b)):
                new.append(b[i])
        elif axis == 1:
            for i in range(len(a)):
                new.append(a[i])
            for i in range(len(b)):
                for y in range(len(b[i])):
                    new[i].append(b[i][y])
        return(new)
    except:
        return(None)
