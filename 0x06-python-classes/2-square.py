#!/usr/bin/python3
"""Module to contain the Square class"""


class Square:

    """The Square class"""
    def __init__(self, size=0):
        """Intitializes Square object and provide size validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
