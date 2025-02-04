#!/usr/bin/env python3
"""defining a single neuron performing binary classification"""
import numpy as np


class Neuron:
    """defining a single neuron"""
    def __init__(self, nx):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.nx = nx
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """getter method"""
        return self.__W

    @property
    def b(self):
        """getter method"""
        return self.__b

    @property
    def A(self):
        """getter method"""
        return self.__A

    def forward_prop(self, X):
        """forward propagation for the neuron"""
        z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-z))
        return self.__A
