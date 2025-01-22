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
        k = int(k)
        if k < 0:
            return 0

        mean_w_k = mean**k
        e_w_neg_mean = e**-mean
        fact_k = factorial(k)

        prob = mean_w_k * e_w_neg_mean / fact_k
        return prob

def factorial(x):
        """a function that calculates factorials"""
        result = x
        for i in range(1, x + 1):
            result *= i
        return result