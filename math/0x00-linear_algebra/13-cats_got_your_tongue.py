#!/usr/bin/env python3
"""contcatinate axis"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """np cat axis in dim"""
    return(np.concatenate((mat1, mat2), axis=axis))
