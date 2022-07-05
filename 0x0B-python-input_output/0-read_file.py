#!/usr/bin/python3
"""Module for reading a function that read a file"""

def read_file (filename=""):
    """Reads a file and print to the standard output"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
