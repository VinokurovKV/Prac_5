from decimal import *

def esum(N, one):
    Type = type(one)
    e = one
    f = one
    for n in range(1, N + 1):
        f *= n
        e += one / f
    return e

print(esum(10, Decimal(1)))
print(esum(10, float(1)))
