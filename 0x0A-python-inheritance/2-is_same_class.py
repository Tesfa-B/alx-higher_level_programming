def is_same_class(obj, a_class):
    """
    check if object is an indtance of a given class
    """
    return type(obj) == type(a_class())
