"""This module creates a class square to define square of numbers"""
class Square:
    """creating a class"""
    def __init__(self, size=0):
        """initializes the square"""
        self.__size = size
        @property
        def size(self):
            """Gets the size of a square"""
            return self.__size
        
        @size.setter
        def size(self, new__size):
            """sets the size of the square"""
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = new__size
    def area(self):
        """computes the area of a square"""
        return self.__size * self.__size    