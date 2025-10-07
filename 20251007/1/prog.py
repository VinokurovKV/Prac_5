from fractions import Fraction

def func(s, w, *args):
  s = Fraction(s)
  w = Fraction(w)
  A = Fraction(0)
  B = Fraction(0)

  deg_a = int(args[0])
  i = 1
  while deg_a >= 0:
    A += Fraction(args[i]) * (s ** deg_a)
    i += 1
    deg_a -= 1

  deg_b = int(args[i])
  i += 1
  while deg_b >= 0:
    B += Fraction(args[i]) * (s ** deg_b)
    i += 1
    deg_b -= 1

  if B == 0:
    return False

  return A / B == w

print(func(*input().split(',')))
