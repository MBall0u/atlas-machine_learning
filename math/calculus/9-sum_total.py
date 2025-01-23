#!/usr/bin/env python3
"""calculates sigma"""


def summation_i_squared(n):
    """recursive :P"""
    if n == 0:
        return 0
    return (n**2 + summation_i_squared(n - 1))
