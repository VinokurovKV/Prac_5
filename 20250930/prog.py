from math import *

def Calc(s, t, u):
    def fun1(x):
        return eval(s)
    def fun2(x):
        return eval(t)
    def fun3(x, y):
        return eval(u)
    def fun(x):
        return fun3(fun1(x), fun2(x))
    return fun

s1, s2, s3 = eval(input())
x = eval(input())
res = Calc(s1, s2, s3)
print(res(x))
