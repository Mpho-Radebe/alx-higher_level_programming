#!/usr/bin/python3
"""Module to contain the Square class"""


class Square:

    """The Square class"""
    def size(self, value):
        """Sets the size of a square to the specified size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
   
    def __init__(self, size=0):
        "Instantiate an object of Square class"
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def size(self):
        """Return the size of a squaire"""
        return self.__size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
