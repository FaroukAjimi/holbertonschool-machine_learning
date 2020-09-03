#!/usr/bin/env python3
"""gppp"""


def poly_integral(poly, C=0):
    """gooog"""
    integral = [C]
    for i in range(len(poly)):
        if i != 0:
            s = (poly[i] ** i)/(i+1)
            if s.is_integer():
                integral.append(int(s))
            else:
                integral.append(s)
        else:
            integral.append(poly[i])
    return(integral)
