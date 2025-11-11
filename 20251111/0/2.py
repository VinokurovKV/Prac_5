def istype(typ):
  def decor(f):
      def newfun(*args):
          for i in args:
              if not isinstance(i, typ):
                  raise TypeError
              return f(*args)
      return newfun
  return decor


@istype(str)
def fun(a, b):
    return a*2+b
