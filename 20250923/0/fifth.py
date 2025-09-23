ll = []
while s := input():
    s = eval(s)
    ll.append(list(s))
print(ll)
for i in range(len(ll)):
    for j in range(i + 1, len(ll)):
        ll[i][j], ll[j][i] = ll[j][i], ll[i][j]
print(ll)
for k in ll:
    print(*k)
