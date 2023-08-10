"""This module creates a class square to define square of numbers"""
class Square:
    """creating a class"""
    def __init__(self, size=0):
        """initializes the square"""
        self._size = size
    @property
    def size(self):
        """Gets the size of a square"""
        return self._size
        
    @size.setter
    def size(self, new_size):
        """sets the size of the square"""
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        self._size = new_size
    def area(self):
        """computes the area of a square"""
        return self._size * self._size    