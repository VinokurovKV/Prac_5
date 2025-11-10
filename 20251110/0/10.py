count = 0
class A: pass
class B: pass

class C(A, B): pass
class D(B, A): pass

for i in [A, B, C, D]:
    for j in [A, B, C, D]:
        try:
            class E(i, j): pass
        except TypeError:
            print(i, j, 'error')
        else:
            count += 1

print(count)
