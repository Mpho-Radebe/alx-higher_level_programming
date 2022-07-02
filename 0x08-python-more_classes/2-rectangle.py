#!/usr/bin/python3
"""Module that contains the class Rectangle"""


class Rectangle:
    """Rectangles to a model a rectangle"""
    def __init__(self, width=0, height=0):
        """Initiates a rectangle object"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """A function to get the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """A function to get the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter of a rectangle"""
        return 2 * self.width + 2 * self.height
