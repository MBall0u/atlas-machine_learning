#!/usr/bin/env python3
"""Creating a function that returns the shape of a matrix"""


def matrix_shape(matrix):
    """returns the shape of a given matrix"""
    result_shape = []
    while isinstance(matrix, list):
        result_shape.append(len(matrix))
        matrix = matrix[0]
    return result_shape
