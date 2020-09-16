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
        self.__W = (np.random.randn(1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """W selr"""
        return (self.__W)

    @property
    def b(self):
        """b soof"""
        return (self.__b)

    @property
    def A(self):
        """yoo"""
        return (self.__A)

    def forward_prop(self, X):
        """bin clas"""
        nx, m = np.shape(X)
        mul = np.matmul(self.__W, X) + self.__b
        self.__A = 1/(1 + (np.exp(-mul)))
        return (self.__A)

    def cost(self, Y, A):
        """COST Function"""
        m = Y.shape[1]
        prob = np.multiply(np.log(A),
                           Y) + np.multiply(1 - Y,
                                            np.log(1.0000001 - A))
        cost = -np.sum(prob) / m
        cost = np.squeeze(cost)
        return (cost)

    def evaluate(self, X, Y):
        """EVALAUTE Function"""
        fp = self.forward_prop(X)
        fpr = np.round(fp)
        fpri = fpr.astype(np.int)
        return(fpri, self.cost(Y, fp))

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """gradient"""
        nx, m = np.shape(X)
        db = np.sum((A-Y)/m)
        dw = np.sum((A-Y)*X, axis=1)/m
        self.__W = self.__W - (alpha * dw)
        self.__b = self.__b - (alpha * db)
        return (self.__W, self.__b)
