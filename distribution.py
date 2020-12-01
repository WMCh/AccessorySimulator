import numpy as np

from constant import NORMAL_SCALE_FACTOR


def distribution(low, high, type):
    dist = {
        'uniform': uniform,
        'normal': normal
    }
    return dist[type](low, high)


def uniform(low, high):
    return int(np.random.uniform(low, high))

def normal(low, high):
    scale = low * NORMAL_SCALE_FACTOR
    val = np.random.normal(loc=low, scale=scale)
    if val < low:
        val = low
    elif val > high:
        val = high
    return int(val)
