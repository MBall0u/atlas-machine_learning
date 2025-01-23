#!/usr/bin/env python3
"""creating the binomial distribution"""


class Binomial:
    """the class of the binomial distribution"""
    def __init__(self, data=None, n=1, p=0.5):
        if n < 0:
            raise ValueError("n must be a positive value")
        if 0 > p > 1:
            raise ValueError("p must be greater than 0 and less than 1")
        self.n = n
        self.p = p

        if data is None:
            return
        if not isinstance(data, list):
            raise TypeError("data must be a list")
        if len(data) < 2:
            raise ValueError("data must contain multiple values")
        mean = sum(data) / len(data)
        variance = mean * (1 - (mean / len(data)))
        p = (mean - variance) / mean
        self.n = round(mean / p)
        self.p = mean / self.n
