#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Define a Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Creates a Rectangle object

        Args:
            width (int, optional)
            height (int, optional)

        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def area(self):
        """Computes the area of a Rectangle

        Returns:
            int
        """
        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of a Rectangle

        Returns:
            int
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

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

    @classmethod
    def square(cls, size=0):
        """Creates a Rectangle with equal width and height"""
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Checks which Rectangle has a bigger area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (rect_1.area() > rect_2.area()) or (rect_1.area() == rect_2.area()):
            return rect_1
        else:
            return rect_2

    def __str__(self):
        string = ""

        if self.__width == 0 or self.__height == 0:
            return string

        for i in range(self.__height):
            string += str(self.print_symbol) * self.__width
            string += "\n" if (i != self.__height - 1) else ""

        return string

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
