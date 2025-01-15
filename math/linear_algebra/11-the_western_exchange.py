#!/usr/bin/env python3
"""a function that transposes a given matrix"""


def np_transpose(matrix):
    """returns a transposed version of a given matrix"""
    transpose_matrix = matrix.copy()
    return transpose_matrix.transpose()
