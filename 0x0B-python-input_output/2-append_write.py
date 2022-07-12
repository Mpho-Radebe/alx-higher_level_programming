#!/usr/bin/python3
"""Appends function"""

def append_write(filename="", text=""):
    """Appends text to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
