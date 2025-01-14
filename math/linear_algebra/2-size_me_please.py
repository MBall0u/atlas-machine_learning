#!/usr/bin/env python3
def matrix_shape(matrix):
    result_shape = []
    while isinstance(matrix, list):
        result_shape.append(len(matrix))
        matrix = matrix[0]
    return result_shape