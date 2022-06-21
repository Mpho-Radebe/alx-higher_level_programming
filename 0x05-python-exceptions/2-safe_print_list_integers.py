#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    while index < x:
        try:
            print("{:d}".format(index), end="")
        except ValueError:
            pass
        index += 1
    print()

