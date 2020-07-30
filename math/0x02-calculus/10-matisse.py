#!/usr/bin/env python3
"""derivative"""


def poly_derivative(poly):
    """ ploy derive"""
    t = type(list)
    if type(poly) is not t:
        return(None)
    der = []
    for i in range(len(poly)):
        if type(poly[i]) is not t:
            return(None)
        if i != 0:
            der.append(i * poly[i])
    if der = []:
        return(0)
    return(der)
