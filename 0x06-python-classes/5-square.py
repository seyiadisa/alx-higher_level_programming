#!/usr/bin/python3
"""Square class module"""


class Square:
    """Square class.

    Defines a Square object

    """

    def __init__(self, size=0):
        """

        Args:
            size (int): the length of a side
        """

        self.size = size

    @property
    def size(self):
        """size: returns the value of the __size private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Checks if the value passed in is an int and is greater than 0"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the current square"""
        return self.__size**2

    def my_print(self):
        """Prints a square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
