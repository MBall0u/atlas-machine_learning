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
        self.stddev = variance**0.5

    def z_score(self, x):
        """the z score"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """the x value for a given z"""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """the pdf ofa given x"""
        pi = 3.1415926536
        e = 2.7182818285
        mean = self.mean
        stddev = self.stddev
        exp_num = (x - mean)**2
        exp_don = 2 * stddev**2
        main_exp_eq = -1 * (exp_num / exp_don)
        main_ep_don = (2 * pi * stddev**2)**0.5
        pdf_result = (1 / main_ep_don) * e**main_exp_eq
        return pdf_result
