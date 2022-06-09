#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_key = [key for key in a_dictionary.keys() if a_dictionary.get(key) == value]
    for key in delete_key:
        a_dictionary.pop(key)
    return a_dictionary

