def fib(m, n):
    x1, x2 = 1, 1
    if m == 0 or m == 1:
        if n >= 1:
            yield x1
        if n >= 2:
            yield x2
        x1, x2 = x2, x1 + x2
        for i in range(3, m + n):
            x1, x2 = x2, x1 + x2
            yield x2
    else:
        for i in range(2, m):
            x1, x2 = x2, x1 + x2
        for i in range(m, m + n):
            x1, x2 = x2, x1 + x2
            yield x2

import sys
exec(sys.stdin.read())
