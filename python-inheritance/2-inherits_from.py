"""a module that checks if an object of an instance of a class inherits from a specified class"""
def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False."""
    
    return issubclass(type(obj), a_class) and type(obj) is not a_class