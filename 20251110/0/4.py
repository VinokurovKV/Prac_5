A = type('AA', (), {'__f': 10})
B = type('BB', (A,), {'__f': 20})

a = A()
b = B()
print(a.__f, b.__f)
