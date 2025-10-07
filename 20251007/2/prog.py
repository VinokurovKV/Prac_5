from math import *

def scale(a, b, A, B, x):
  return (x - a) * (B - A) / (b - a) + A

W, H, A, B, func = input().split(" ")
W = int(W)
H = int(H)
A = int(A)
B = int(B)
screen = [[' '] * W for i in range(H)]

x = scale(0, W - 1, A, B, 0)
y = eval(func)
y_min, y_max = y, y

for i in range(1, W):
  x = scale(0, W - 1, A, B, i)
  y = eval(func)
  if y < y_min:
    y_min = y
  if y > y_max:
    y_max = y

for i in range(W):
  x = scale(0, W - 1, A, B, i)
  y = scale(y_min, y_max, H - 1, 0, eval(func))
  screen[int(y)][i] = '*'
  y_prev = int(y)
  if i > 0:
    for j in [*range(int(y) + 1, prev_y), *range(prev_y, int(y))]:
      screen[j][i-1] = '*'
  prev_y = int(y)

print('\n'.join(''.join(line) for line in screen))