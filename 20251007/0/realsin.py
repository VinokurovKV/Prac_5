from math import *

def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A

w, h = eval(input())
a, b = eval(input())
screen = [[' '] * w for i in range(h)]
for i in range(0, w):
    x = scale(0, w - 1, a, b, i)
    y = sin(x)
    k = round(scale(-1, 1, 0, h - 1, y))
    screen[h - k - 1][i] = "*"
    
print('\n'.join(''.join(line) for line in screen))
