ll = []
while s := input():
    s = eval(s)
    ll.append(list(s))
if any([len(k) != len(ll) for k in ll]):
    print("Wrong data")
    exit()


for i in range(len(ll)):
    for j in range(i + 1, len(ll)):
        ll[i][j], ll[j][i] = ll[j][i], ll[i][j]

for k in ll:
    print(*k)
