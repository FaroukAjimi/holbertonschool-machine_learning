#!/usr/bin/env python3
"""derivative"""


def poly_derivative(poly):
    """ ploy derive"""
    t = type([])
    t1 = type(1)
    if type(poly) is not t:
        return(None)
    if len(poly) == 0:
        return(None)
    if len(poly) == 1:
        return([0])
    der = []
    for i in range(len(poly)):
        if i != 0:
            der.append(i * poly[i])
    return(der)
