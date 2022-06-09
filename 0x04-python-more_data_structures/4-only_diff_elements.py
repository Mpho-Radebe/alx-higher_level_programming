#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff1 = list(set.difference(set_1, set_2))
    diff2 = list(set.difference(set_2, set_1))
    return diff1 + diff2
