#!/usr/bin/python3
def magic_string():
    magic_string.c = 1 if not hasattr(magic_string, "c") else magic_string.c + 1
    return  ", ".join([("BestSchool") for i in range(magic_string.c)])
