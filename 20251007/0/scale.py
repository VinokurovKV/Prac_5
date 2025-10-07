from math import *

def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A

w, h = eval(input())
a, b = eval(input())
for line in range(0, h):
    x = line * (b - a) / (h - 1) + a
    scale(0, h - 1, a, b, line)
    y = sin(x)
    k = round(scale(-1, 1, 0, w - 1, y))
    print(" "*k, "*")
