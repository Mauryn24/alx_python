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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
    
    @property
    def height(self):
        """get the height of rectangle"""
        return self.__height
    
    @height.setter
    def height(self, height):
        """set height of the rectangle"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        
    @property
    def x(self):
        """Get the x-coordinate of the rectangle"""
        return self.__x
    
    @x.setter
    def x(self, x):
        """Set the x coordinate"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        
    @property
    def y(self):
        """Get the Y-coordinate"""
        return self.__y
    
    @y.setter
    def y(self, y):
        """Set the y-coordinate"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.validate_width(width)
        self.validate_height(height)
        self.validate_x(x)
        self.validate_y(y)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate_width(self, width):
        """Validate the width of the rectangle."""
        if not isinstance(width, int):
            raise TypeError("Width must be an integer.")
        if width <= 0:
            raise ValueError("Width must be > 0.")

    def validate_height(self, height):
        """Validate the height of the rectangle."""
        if not isinstance(height, int):
            raise TypeError("Height must be an integer.")
        if height <= 0:
            raise ValueError("Height must be > 0.")

    def validate_x(self, x):
        """Validate the x-coordinate of the rectangle."""
        if not isinstance(x, int):
            raise TypeError("X-coordinate must be an integer.")
        if x < 0:
            raise ValueError("X-coordinate must be >= 0.")

    def validate_y(self, y):
        """Validate the y-coordinate of the rectangle."""
        if not isinstance(y, int):
            raise TypeError("Y-coordinate must be an integer.")
        if y < 0:
            raise ValueError("Y-coordinate must be >= 0.")