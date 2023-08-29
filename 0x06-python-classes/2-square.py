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

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
