#!/usr/bin/env python3
"""derivative"""


def poly_derivative(poly):
    """ ploy derive"""
    der = []
    for i in range(len(poly)):
        if i != 0:
            der.append(i * poly[i])
    return(der)
