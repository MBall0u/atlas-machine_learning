#!/usr/bin/env python3
"""creating the poisson distribution"""


class Poisson:
    """the class representation of the poisson distribution"""
    def __init__(self, data=None, lambtha=1.):
        self.lambtha = lambtha

        if data is None:
            return
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        if not isinstance(data, list):
            raise TypeError("data must be a list")
        if len(data) < 2:
            raise ValueError("data must contain multiple values")
        self.lambtha = sum(data) / len(data)
