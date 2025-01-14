#!/usr/bin/env python3
"""write a function that adds two 2D matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """returns a matrix of the result of adding two matrices"""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    result_matrix = [[0 for _ in range(len(mat1[0]))]
                     for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result_matrix[i][j] = mat1[i][j] + mat2[i][j]
    return result_matrix
