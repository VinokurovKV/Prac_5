from decimal import *
from fractions import *
def multiplier(x, y, Type):
    if Type == float:
        return float(x) * float(y)
    elif Type == Decimal:
        return Decimal(x) * Decimal(y)
    else:
        return Fraction(x) * Fraction(y)

a, b = eval(input())
print(multiplier(a, b, float))
print(multiplier(a, b, Decimal))
print(multiplier(a, b, Fraction))
