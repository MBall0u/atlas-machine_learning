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
        if isinstance(data, list):
            raise TypeError("data must be a list")
        if len(data) < 2:
            raise ValueError("data must contain multiple values")
        p = sum(data) / len(data)
        n = round(sum(data) / p)
        p = sum(data) / n

        self.n = n
        self.p = p
