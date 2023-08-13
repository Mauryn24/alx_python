"""A module that creates a class Rectangle which is a child of BaseGeometry"""
class BaseGeometry:
    """class Geometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
class Rectangle(BaseGeometry):
    """A class Rectangle which is a child of BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
    def area(self):
        return self.__width * self.__height
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
class Square(Rectangle):
    """Class Square which is a child of Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
    def area(self):
        return self.__size * self.__size