def genf(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / (i * i)
        yield s

e = genf(int(input()))
print(*e)
