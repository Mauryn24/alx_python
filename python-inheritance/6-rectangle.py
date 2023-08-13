"""a module that create a rectangle which inherits from BaseGeometry"""
def Rectangle(BaseGeometry):
    """class Rectangle which is a child of BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)