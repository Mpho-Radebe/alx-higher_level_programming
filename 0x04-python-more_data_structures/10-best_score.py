#!/usr/bin/python3
def best_score(a_dictionary):
    d = a_dictionary
    max_key = None
    for key in d.keys():
        if max_key is None or d.get(max_key) =< d.get(key):
            max_key = key
    return max_key
