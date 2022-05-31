#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ch >= 'a' and ch <= 'z':
            ch = chr(ord(ch) - 32)
        print("{}".format(ch), end="")
    print()
