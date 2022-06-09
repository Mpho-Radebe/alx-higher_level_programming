#!/usr/bin/python3
def uniq_add(my_list=[]):
    l1 = my_list
    n = range(len(my_list))
    l2 = [l1[i] for i in n if not l1[i] in l1[(i + 1):]]
    return sum(l2)
