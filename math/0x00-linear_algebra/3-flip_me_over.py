#!/usr/bin/env python3
def matrix_transpose(matrix):
    new = []
    for i in matrix[0]:
        new.append([])
    nd = len(matrix[0])
    for i in range(nd):
        for y in range(len(matrix)):
            new[i].append(matrix[y][i])
    return(new)
