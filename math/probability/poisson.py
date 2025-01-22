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
        neg_mean = -1 * mean
        k = int(k)
        if k < 0:
            return 0

        mean_w_k = mean**k
        e_w_neg_mean = e**neg_mean
        fact_k = 1
        for i in range(1, k + 1):
            fact_k *= i

        prob = mean_w_k * e_w_neg_mean / fact_k
        return prob

    def cdf(self, k):
        """calculates the cdf for the given k"""
        k = int(k)
        if k < 0:
            return 0

        sum = 0.0
        for x in range(k + 1):
            sum += self.pmf(x)

        return sum
