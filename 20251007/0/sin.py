from math import *

w, h = eval(input())
a, b = eval(input())
for line in range(0, h):
    x = line * (b - a) / (h - 1) + a
    y = sin(x)
    k = round((y + 1) * (w - 1) / 2)
    print(" "*k, "*")
