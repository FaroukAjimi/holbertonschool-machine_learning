#!/usr/bin/env python3
""" mat"""
def mat_mul(mat1, mat2):
    """mull"""
    new = []
    fin = []
    eq = len(mat2[0])
    for i in range(len(mat1)):
        new.append([])
    for i in range(len(mat1)):
        fin.append([])
    for x in range(len(mat1)):
        for y in range(len(mat1[0])):
            for z in range(len(mat2[0])):
                new[x].append(mat1[x][y] * mat2[y][z])
    n = int(len(new[i]) / 2)
    for i in range(len(new)):
        for y in range(n): 
            fin[i].append(new[i][y] + new[i][y + eq])
    return(fin)
