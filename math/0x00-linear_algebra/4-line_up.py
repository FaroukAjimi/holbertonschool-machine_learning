#!/usr/bin/env python3
"""task 4"""


def add_arrays(arr1, arr2):
    """add"""
    new = []
    if len(arr1) != len(arr2):
        return(None)
    if arr1 == [] or arr2 == []:
        return(None)
    if len(arr1) != len(arr2):
        return(None)
    for i in range(len(arr1)):
        new.append(arr1[i] + arr2[i])
    return(new)
