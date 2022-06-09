#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weights = 0
    weighted_sum = 0
    for (s, w) in my_list:
        weighted_sum += s * w
        weights += w
    return weighted_sum / weights
