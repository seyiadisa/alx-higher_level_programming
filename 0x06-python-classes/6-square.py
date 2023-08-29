#!/usr/bin/python3
"""Square class module"""


class Square:
    """Square class.

    Defines a Square object

    """

    def __init__(self, size=0, position=(0, 0)):
        """

        Args:
            size (int): the length of a side
            position (tuple of int):
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Returns the private attribute: position"""
        return self.__position

    @position.setter
    def position(self, value: tuple):
        """Sets the private attribute position"""
        if type(value) is not tuple or not all(
            type(n) is int and n >= 0 for n in value
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the current square"""
        return self.__size**2

    def my_print(self):
        """Prints a square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
