import itertools

def divn(n, seq):
    yield from itertools.filterfalse(lambda x: x % n, seq)


