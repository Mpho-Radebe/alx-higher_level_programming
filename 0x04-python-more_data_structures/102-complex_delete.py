#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dic = a_dictionary
    delete_key = [key for key in a_dic.keys() if a_dic.get(key) == value]
    for key in delete_key:
        a_dictionary.pop(key)
    return a_dictionary

