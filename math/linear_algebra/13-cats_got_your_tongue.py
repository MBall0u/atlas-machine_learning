#!/usr/bin/env python3
"""a function that concatenates two matrices"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """returns a concatenated matrix on a given axis"""
    return np.concatenate((mat1, mat2), axis=axis)
