class A:
    v = 1

class B(A):
    v = 2

b = B()
b.v = 3

print(A.v, B.v, b.v)

del b.v
print(A.v, B.v, b.v)

del B.v
print(A.v, B.v, b.v)
