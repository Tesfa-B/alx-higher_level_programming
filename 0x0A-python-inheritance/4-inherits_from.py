def inherits_from(obj, a_class):
    """
    checks the object class is inherited from specfied class    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
