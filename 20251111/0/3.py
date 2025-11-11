class IsType:
  def __init__(self, typ):
    self.typ = typ
  
  def __call__(self, function):
    def newfun(*args):
      for i in args:
        if not isinstance(i, self.typ):
          raise TypeError
        return function(*args)
    return newfun
    
@IsType(int)
def fun(a, b):
    return a*2+b