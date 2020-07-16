#!/usr/bin/env python3
"""task 4"""


def add_arrays(arr1, arr2):
    """add arr1 + arr2"""
    if len(arr1) != len(arr2):
        return None
    new = []
    for i in range(len(arr1)):
        new.append(arr1[i] + arr2[i])
    return new
