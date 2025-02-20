#!/usr/bin/env python3
"""adds a layer"""
import tensorflow.compat.v1 as tf


def create_layer(prev, n, activation):
    """creates a layer"""
    layer = tf.layers.dense(prev, units=n, activation=activation, name="layer")
    return layer
