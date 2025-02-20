#!/usr/bin/env python3
"""everything for a neural network"""
import numpy as np


class NeuralNetwork:
    """defines a neural network with one hidden layer"""
    def __init__(self, nx, nodes):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """getter method"""
        return self.__W1

    @property
    def b1(self):
        """getter method"""
        return self.__b1

    @property
    def A1(self):
        """getter method"""
        return self.__A1

    @property
    def W2(self):
        """getter method"""
        return self.__W2

    @property
    def b2(self):
        """getter method"""
        return self.__b2

    @property
    def A2(self):
        """getter method"""
        return self.__A2

    def forward_prop(self, X):
        """forward propagation for the neural network"""
        z1 = np.dot(self.__W1, X) + self.__b1
        self.__A1 = 1 / (1 + np.exp(-z1))
        z2 = np.dot(self.__W2, self.__A1) + self.__b2
        self.__A2 = 1 / (1 + np.exp(-z2))
        return self.__A1, self.__A2
