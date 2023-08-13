"""A module that creates a base class for managing id attributes"""
class Base:
    """Base class for managing id attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor fo Base Class.
        if id is not None, assign
        the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects