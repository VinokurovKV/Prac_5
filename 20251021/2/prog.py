import itertools

def slide(seq, n):
    first, second = itertools.tee(seq)
    pos = 0
    while True:
        window = list(itertools.islice(first, pos, pos + n))
        if not window:
            return
        yield from window
        first, second = itertools.tee(second)
        pos += 1

import sys
exec(sys.stdin.read())