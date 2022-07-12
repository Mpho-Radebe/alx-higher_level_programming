#!/usr/bin/python3
"""Module that write something to a file"""

def write_file(filename="", text=""):
    """Write a text into a file with the given filename"""
    with open(filename, "r", encoding="utf-8") as f:
        return f.write(text)
