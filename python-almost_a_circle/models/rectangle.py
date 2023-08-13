"""A module that makes a child class Rectangle"""
from models.base import Base

class Rectangle(Base):
    """child class Rectangle"""

    __width = None
    __height = None
    __x = None
    __y = None

    @property
    def width(self):
        """Get the width of a rectangle"""
        return self.__width
    
    @width.setter
    def width(self, width):
        """set width of a rectangle"""
        if width < 0:
            raise ValueError("Width must be non_negative.")
        self.__width = width
    
    @property
    def height(self):
        """get the height of rectangle"""
        return self.__height
    
    @height.setter
    def height(self, height):
        """set height of the rectangle"""
        if height < 0:
            raise ValueError("Height must be a non-negative")
        self.__height = height

    @property
    def x(self):
        """Get the x-coordinate of the rectangle"""
        return self.__x
    
    @x.setter
    def x(self, x):
        """Set the x coordinate"""
        if x < 0:
            raise ValueError(" X-coordonate must be non-negative")
        self.__x = x

    @property
    def y(self):
        """Get the Y-coordinate"""
        return self.__y
    
    @y.setter
    def y(self, y):
        """Set the y-coordinate"""
        if y < 0:
            raise ValueError("Y-coordinate must be a non-negative")
        self.__y = y
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y