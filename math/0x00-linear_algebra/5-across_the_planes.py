#!/usr/bin/env python3
def add_matrices2D(mat1, mat2):
    new = []
    if (len(mat1) != len(mat2)) or (len(mat1[0]) != len(mat2[0])):
        return(None)
    for i in range(len(mat1)):
        new.append([])
        for y in range(len(mat2)):
            new[i].append(mat1[i][y]+mat2[i][y])
    return(new)
