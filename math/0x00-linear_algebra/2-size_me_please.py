#!/usr/bin/env python3
def matrix_shape(matrix):
    a= []
    c=[]
    t = type(a)
    while True:
        if type(matrix) is t:
            c.append(len(matrix))
            matrix = matrix[0]
        else:
            break
    return(c)
