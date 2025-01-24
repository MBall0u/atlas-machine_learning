#!/usr/bin/env python3
"""line graph"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """line graph"""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(range(11), y, 'r-')
    plt.xlim(0, 10)
    plt.show()
