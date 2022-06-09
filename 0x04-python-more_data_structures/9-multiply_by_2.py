#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    double_dict = dict();
    for key in a_dictionary.keys():
        double_dict[key] = a_dictionary.get(key) * 2
    return double_dict
