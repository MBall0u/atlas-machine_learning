#!/usr/bin/env python3
"""adds a layer"""
import tensorflow.compat.v1 as tf


def create_layer(prev, n, activation):
    """creates a layer"""
    init = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    layer = tf.keras.layers.Dense(
        units=n,
        activation=activation,
        name="layer",
        kernel_initializer=init
    )
    return layer(prev)
