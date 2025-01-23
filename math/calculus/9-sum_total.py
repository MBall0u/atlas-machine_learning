#!/usr/bin/env python3
"""calculates sigma"""


def summation_i_squared(n):
    """might not work wit the for loop :)"""
    result = 0
    for i in range(1, n):
        result += i**2
    return result
