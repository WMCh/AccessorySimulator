import random

import numpy as np

from distribution import distribution as dist
from constant import *


def generate_main_prop(level, type, distribution='normal'):
    prop_type = random.choice(MAIN_PROP[type])
    if type == 'accessory':
        low = MAIN_PROP_VAL[type][0] * level + MAIN_PROP_VAL[type][1]
        high = MAIN_PROP_VAL[type][2] * level + MAIN_PROP_VAL[type][3]
    else:
        low = MAIN_PROP_VAL[type][0] * level
        high = MAIN_PROP_VAL[type][1] * level
    prop_val = dist(low, high, distribution)
    return prop_type, prop_val

def generate_addition_prop(level, type, p_add3=P_ADD_3, distribution='normal'):
    add_list = []

    add1_type = random.choice(ADDITION_PROP[type])
    add1_val = generate_addition_val(level, add1_type, distribution)
    add_list.append((add1_type, add1_val))

    add2_type = random.choice(ADDITION_PROP[type])
    add2_val = generate_addition_val(level, add2_type, distribution)
    add_list.append((add2_type, add2_val))

    if np.random.random() < p_add3:
        add3_type = random.choice(ADDITION_PROP[type])
        add3_val = generate_addition_val(level, add3_type, distribution)
        add_list.append((add3_type, add3_val))
    
    return add_list

def generate_addition_val(level, add_type, distribution='normal'):
    if add_type in ADDITION_CATE[0]:
        low = ADDITION_PROP_VAL[0][0] * level + ADDITION_PROP_VAL[0][1]
        if level in [60, 80]:
            high = low + 3
        elif level in [100, 120]:
            high = low + 4
        else:
            high = low + 5
    else:
        for i in range(1, 4):
            if add_type in ADDITION_CATE[i]:
                low = ADDITION_PROP_VAL[i][0] * level
                high = ADDITION_PROP_VAL[i][1] * level
    add_val = dist(low, high, distribution)
    return add_val

def generate_special_effect():
    se = None
    if np.random.random() < P_SPECIAL_EFFECT:
        se = random.choice(SPECIAL_EFFECT)
    return se
