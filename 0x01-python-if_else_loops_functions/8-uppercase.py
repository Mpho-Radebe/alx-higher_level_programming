#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        print("{}".format(chr(ord(ch) - 32) if ord(ch) >= ord('a') and ord(ch) <= ord('z') else ch, end=""))
    print()
