#!/usr/bin/env python3
"""contcatinate axis"""


def np_cat(mat1, mat2, axis=0):
    """np cat axis in dim"""
    return(np.concatenate((mat1, mat2), axis=axis))
