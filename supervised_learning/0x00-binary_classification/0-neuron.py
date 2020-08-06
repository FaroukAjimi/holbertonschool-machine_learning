#!/usr/bin/env python3
"""Supervised leaning intro"""


import numpy as np


class Neuron:
    """Class neuron"""
    def __init__(self, nx):
        "init func"""
        if not(isinstance(nx, int)):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.W = (np.random.randn(1, nx))
        self.b = 0
        self.A = 0
