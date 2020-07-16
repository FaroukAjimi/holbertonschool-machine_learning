#!/usr/bin/env python3
"""imprt"""
import numpy as np
def np_cat(mat1, mat2, axis=0):
    """np cat"""
    return(np.concatenate((mat1,mat2), axis=axis))
