def isint(f):
    def newfun(*args):
        for i in args:
            if type(i) != int:
                raise TypeError
            return f(*args)
    return newfun


@isint
def fun(a, b):
    return a*2+b

