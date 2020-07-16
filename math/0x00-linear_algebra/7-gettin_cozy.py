#!/usr/bin/env python3
"""copet cat matrice"""


def cat_matrices2D(mat1, mat2, axis=0):
    """ cat mat 2d"""
    new = []
    lis1 = []
    try:
        if axis == 0:
            for i in range(len(mat1)):
                new.append(mat1[i])
            for i in range(len(mat2)):
                new.append(mat2[i])
        elif axis == 1:
            for i in range(len(mat1)):
                new.append(mat1[i])
            for i in range(len(mat2)):
                for y in range(len(mat2[i])):
                    new[i].append(mat2[i][y])
        return(new)
    except:
        return(None)
