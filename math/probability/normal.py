#!/usr/bin/env python3
"""creating the normal distribution"""


class Normal:
    """class representation of the normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        if stddev <= 0:
            raise ValueError("stddev must be a positive value")
        self.stddev = stddev
        self.mean = mean


        if data is None:
            return
        if not isinstance(data, list):
            raise TypeError("data must be a list")
        if len(data) < 2:
            raise ValueError("data must contain multiple values")
        self.mean = sum(data) / len(data)
        variance = sum((x - self.mean) ** 2 for x in data) / len(data)
        self.stddev = variance**variance
