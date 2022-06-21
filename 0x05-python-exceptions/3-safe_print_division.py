#!/usr/bin/python3
def safe_print_division(a, b):
    div = None
    try:
       div = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: ")
        if div == None:
            print("None")
        else:
            print("{}".format(div))
        return div

