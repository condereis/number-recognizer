# -*- coding: utf-8 -*-
import click
import json
import numpy as np
import os
import pandas as pd
import sys
import tensorflow as tf



def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1], padding='SAME')

def read_number(inputs_list):
    tf.reset_default_graph()
    # Imput layer
    x = tf.placeholder(tf.float32, shape=[None, 784])
    x_image = tf.reshape(x, [-1, 28, 28, 1])

    # Convolutional layer 1
    W_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)

    # Pooling 1
    h_pool1 = max_pool_2x2(h_conv1)

    # Convolutional layer 2
    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)

    # Pooling 2
    h_pool2 = max_pool_2x2(h_conv2)

    # Fully conected layer
    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    b_fc1 = bias_variable([1024])
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    # Dropout and softmax
    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
    W_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])
    y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

    # Predict
    saver = tf.train.Saver()
    with tf.Session() as sess:
        # Restore variables from disk.
        model_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "conv_nn.ckpt"
        )
        saver.restore(sess, model_path)
        predict = sess.run(
            y_conv, feed_dict={x: inputs_list / 255.0, keep_prob: 1.0}
        )

    pred = [np.argmax(one_hot_list) for one_hot_list in predict]
    pred = map(str, pred)
    return int("".join(pred))

