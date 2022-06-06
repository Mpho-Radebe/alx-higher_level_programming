#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = []
    if idx >= 0 and idx < len(my_list):
        for i in range(0, len(my_list)):
            if i == idx:
                copy.append(element)
            else:
                copy.append(my_list[i])
    if idx == len(my_list):
        copy.append(element)
    return copy
