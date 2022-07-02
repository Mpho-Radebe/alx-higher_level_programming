#!/usr/bin/python3
"""Module to contain the Square class"""


class Square:

    """The Square class"""
    def __init__(self, size=0):
        """Sets the size of a square to the specified size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Return the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        "Instantiate an object of Square class"
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __lt__(self, other):
        """returns this < other"""
        return self.area() < other.area()

    def __le__(self, other):
        """returns this <= other"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """returns this == other"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Returns this != other"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Returns this > other"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Returns this >= other"""
        return self.area() >= other.area()
