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

    def cost(self, Y, A):
        """calculates the cost of the model using logestic regression"""
        cost = -np.sum(np.multiply(np.log(A), Y) + np.multiply(
            np.log(1.0000001 - A), (1 - Y))) / Y.shape[1]
        return cost

    def evaluate(self, X, Y):
        """evaluates the neuron's predictions"""
        fp = self.forward_prop(X)
        return np.where(fp >= 0.5, 1, 0), self.cost(Y, fp)
