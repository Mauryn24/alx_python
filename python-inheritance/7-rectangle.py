"""A module that creates a class Rectangle which is a child of BaseGeometry"""
def Rectangle(BaseGeometry):
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