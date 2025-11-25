import inspect
class Check:
    a: int
    def __init__(self, value):
        if not isinstance(value, inspect.get_annotations(self.__class__)['a']):
            raise TypeError    
        self.a = value
