#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as err:
        sys.stderr.write(str(err) + "\n")
        return False
    else:
        return True
