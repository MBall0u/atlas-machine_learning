#!/usr/env/bin python3
"""defining a single neuron performing binary classification"""
import numpy as np


class Neuron:
    """defining a single neuron"""
    def __init__(self, nx):
        if not int(nx):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.nx = nx
        self.W = np.random.randn
        self.b = 0
        self.A = 0
