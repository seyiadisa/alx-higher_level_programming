#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Define a Rectangle class"""

    def __init__(self, width=0, height=0):
        """Creates a Rectangle object

        Args:
            width (int, optional)
            height (int, optional)

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width property"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
