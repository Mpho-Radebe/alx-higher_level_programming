#!/usr/bin/python3
def best_score(a_dictionary):
    max = None
    for key in a_dictionary.keys():
        if max is None or a_dictionary.get(max) < a_dictionary.get(key):
            max = key
    return key
