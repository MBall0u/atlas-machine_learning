#!/usr/bin/env python3
"""a function that returns a tuple of addition, subtraction, multiplication, and division"""


def np_elementwise(mat1, mat2):
    """returns matrix addition, subtraction, multiplication, and division"""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
