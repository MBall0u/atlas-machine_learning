#!/usr/bin/env python3
"""creating the poisson distribution"""


class Poisson:
    """the class representation of the poisson distribution"""
    def __init__(self, data=None, lambtha=1.):
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        self.lambtha = lambtha

        if data is None:
            return
        if not isinstance(data, list):
            raise TypeError("data must be a list")
        if len(data) < 2:
            raise ValueError("data must contain multiple values")
        self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """calculates the pmf for the given k"""
        e = 2.7182818285
        mean = self.lambtha

        prob = ((mean**(int(k)))(e**(-mean)) / (factorial(int(k))))
        return prob

def factorial(x):
        """a function that calculates factorials"""
        result = x
        for i in range(1, n + 1):
            result *= i
        return result