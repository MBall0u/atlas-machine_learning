#!/usr/bin/env python3
"""adds a layer"""
import tensorflow as tf


def create_layer(prev, n, activation):
    """creates a layer"""
    layer = tf.keras.layers.Dense(prev, units=n, activation=activation, name="layer")
    return layer
