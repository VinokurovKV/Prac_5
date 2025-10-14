c = {}
for w in input().split():
    c[w] = c.setdefault(w, 1) + 1
print(c)
