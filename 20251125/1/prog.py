class dump(type):
    def __new__(cls, name, bases, dct):
        new_dct = {}
        
        for attr_name, attr_value in dct.items():
            if callable(attr_value):
                def create_wrapper(method):
                    def wrapper(self, *args, **kwargs):
                        filtered_args = tuple(arg for arg in args if isinstance(arg, (str, int, float, bool)))
                        filtered_kwargs = {k: v for k, v in kwargs.items() if isinstance(v, (str, int, float, bool))}
                        
                        print(f"{method.__name__}: {filtered_args}, {filtered_kwargs}")
                        
                        return method(self, *args, **kwargs)
                    return wrapper
                
                wrapped_method = create_wrapper(attr_value)
                wrapped_method.__name__ = attr_value.__name__
                new_dct[attr_name] = wrapped_method
            else:
                new_dct[attr_name] = attr_value
        
        return super().__new__(cls, name, bases, new_dct)

import sys
exec(sys.stdin.read())