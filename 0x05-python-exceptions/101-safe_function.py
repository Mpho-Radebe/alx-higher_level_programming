#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        fct(*args)
    except Exception as ex:
        sys.stderr.write("Exception: " + str(e) + "\n")
