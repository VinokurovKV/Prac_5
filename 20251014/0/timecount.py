from collections import Counter
import timeit

def counter(s):
    return Counter(s)

def dict(s):
    c = {}
    for w in s:
        c[w] = c.get(w, 1) + 1
    return c

s = input().split()
t1 = timeit.Timer('counter(s)', globals=globals())
t2 = timeit.Timer('dict(s)', globals=globals())
print(t1.autorange(), t2.autorange())
