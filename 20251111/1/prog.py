def objcount(cls):
    cls.counter = 0
    
    old_init = cls.__init__ if hasattr(cls, '__init__') else None
    old_del = cls.__del__ if hasattr(cls, '__del__') else None
    
    def new_init(self, *args, **kwargs):
        cls.counter += 1
        if old_init:
            old_init(self, *args, **kwargs)
    
    def new_del(self):
        cls.counter -= 1
        if old_del:
            old_del(self)
    
    cls.__init__ = new_init
    cls.__del__ = new_del
    
    return cls

import sys
exec(sys.stdin.read())