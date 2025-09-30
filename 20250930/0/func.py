from math import *

def MINF(*funs):
    def fun(x):
        return min([f(x) for f in funs])
    return fun

g = MINF(sin, cos, tan)
print(g(0.4))
        
