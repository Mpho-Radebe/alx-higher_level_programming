#!/usr/bin/python3
def best_score(a_dictionary):
    d = a_dictionary
    first = True
    max_key = None
    for key in d.keys():
        if first or d.get(max_key) < d.get(key):
            max_key = key
        first = False
    return max_key
