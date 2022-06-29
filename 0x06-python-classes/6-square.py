#!/usr/bin/python3
"""Module to contain the Square class"""


class Square:

    """The Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Sets the size of a square to the specified size"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Property for the retrieving the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property for setteing the size of a square"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)

    def __str__(self):
        """Returns a string a of this square"""
        str_rep = ""
        if self.size == 0:
            str_rep += "\n"
        else:
            for i in range(self.position[1]):
                str_rep += "\n"
            for i in range(self.size):
                str_rep += " " * self.position[0]
                str_rep += "#" * self.size + "\n"
        return str_rep

    def __repr__(self):
        """Returns a string of this square"""
        return str(self)
