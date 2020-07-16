#!/usr/bin/env python3
"""across matrice system"""


def add_matrices2D(mat1, mat2):
    """add 2d matrix"""
    new = []
    if (len(mat1) != len(mat2)):
        return(None)
    for i in range(len(mat1)):
        if len(mat1[i]) != len(mat2[i]):
               return None
    for i in range(len(mat1)):
        new.append([])
        for y in range(len(mat2)):
            new[i].append(mat1[i][y]+mat2[i][y])
    return(new)
