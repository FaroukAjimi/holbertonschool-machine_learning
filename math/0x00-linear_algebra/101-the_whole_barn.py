#!/usr/bin/env python3
"""add matrix"""


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


def add_matrices(mat1, mat2):
    """add matrice - function
    @mat1: first matrix
    @mat2: second matrix"""
    lis = []
    lnth = matrix_shape(mat1)
    if (lnth != matrix_shape(mat2)):
        return(None)
    if len(lnth) == 1:
        for i in range(lnth[0]):
            s = mat1[i] + mat2[i]
            lis.append(s)
    else:
        for matrix1, matrix2 in zip(mat1, mat2):
            lis.append(add_matrices(matrix1, matrix2))
    return(lis)
