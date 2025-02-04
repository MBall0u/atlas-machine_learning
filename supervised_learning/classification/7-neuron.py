#!/usr/bin/env python3
"""defining a single neuron performing binary classification"""
import numpy as np
import matplotlib.pyplot as plt


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

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """calculates one pass gradient descent"""
        dz = A - Y
        dw = np.dot(dz, X.T) / Y.shape[1]
        db = np.sum(dz) / Y.shape[1]

        self.__W -= alpha * dw
        self.__b -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):
        """trains the neuron"""
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        if verbose or graph:
            if not isinstance(step, int):
                raise TypeError("step must be an integer")
            if step <= 0 or step > iterations:
                raise ValueError("step must be positive and <= iterations")

        steps = []
        costs = []
        for i in range(iterations):
            A = self.forward_prop(X)
            if verbose:
                if i % step == 0 or i == 0:
                    cost = self.cost(Y, A)
                    costs.append(cost)
                    steps.append(i)
                    print(f"Cost after {i} iterations: {cost}")
            self.gradient_descent(X, Y, A, alpha)

        plt.plot(steps, costs)
        plt.title("Training Cost")
        plt.xlabel("iteration")
        plt.ylabel("cost")
        plt.show()
        return self.evaluate(X, Y)
