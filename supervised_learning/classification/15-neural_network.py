#!/usr/bin/env python3
"""everything for a neural network"""
import numpy as np
import matplotlib.pyplot as plt


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

    def cost(self, Y, A):
        """calculates the cost of the model using logestic regression"""
        cost = -np.sum(np.multiply(np.log(A), Y) + np.multiply(
            np.log(1.0000001 - A), (1 - Y))) / Y.shape[1]
        return cost

    def evaluate(self, X, Y):
        """evaluates the neuron's predictions"""
        _, fp = self.forward_prop(X)
        return np.where(fp >= 0.5, 1, 0), self.cost(Y, fp)

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """calculates one pass gradient descent"""
        dz2 = A2 - Y
        dw2 = np.dot(dz2, A1.T) / Y.shape[1]
        db2 = np.sum(dz2, axis=1, keepdims=True) / Y.shape[1]

        dz1 = (self.__W2.T * dz2) * (A1 * (1 - A1))
        dw1 = np.dot(dz1, X.T) / Y.shape[1]
        db1 = np.sum(dz1, axis=1, keepdims=True) / Y.shape[1]

        self.__W1 -= alpha * dw1
        self.__b1 -= alpha * db1
        self.__W2 -= alpha * dw2
        self.__b2 -= alpha * db2

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):
        """trains the neural network"""
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")
        if verbose or graph:
            if not isinstance(step, int):
                raise TypeError("step must be an integer")
            if step < 0 and step <= iterations:
                raise ValueError("step must be positive and <= iterations")

        steps = []
        costs = []
        for i in range(iterations):
            A1, A2 = self.forward_prop(X)
            if verbose:
                if i % step == 0 or i == 0 or i == (len(step) - 1):
                    cost = self.cost(Y, A2)
                    costs.append(cost)
                    steps.append(i)
                    print(f"Cost after {i} iterations: {cost}")
            self.gradient_descent(X, Y, A1, A2, alpha)

        if graph:
            plt.plot(steps, costs)
            plt.title("Training Cost")
            plt.xlabel("iteration")
            plt.ylabel("cost")
            plt.show()

        return self.evaluate(X, Y)
