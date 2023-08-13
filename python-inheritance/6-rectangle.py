"""a module that create a rectangle which inherits from BaseGeometry"""
def Rectangle(BaseGeometry):
    """class Rectangle which is a child of BaseGeometry"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height