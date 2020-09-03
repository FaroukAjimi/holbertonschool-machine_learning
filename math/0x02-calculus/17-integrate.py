#!/usr/bin/env python3
"""gppp sdo sdoo"""


def poly_integral(poly, C=0):
    """gooog
    sdsqd
    dsqd
    """
    integral = [C]
    if not(isinstance(poly, list)) or not(isinstance(C, int)):
        return(None)
    if len(poly) == 0 or poly is None:
        return(None)
    if poly == [0]:
        return([C])
    for i in range(len(poly)):
        if i != 0:
            s = poly[i] / (i+1)
            if s.is_integer():
                integral.append(int(s))
            else:
                integral.append(s)
        else:
            integral.append(poly[i])
    return(integral)
