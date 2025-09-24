lst = []
while s := input():
    lst.append(eval(s))
n = len(lst[0])
m1, m2 = [], []
for i in range(n):
    m1.append(lst[i])
for i in range(n, 2 * n):
    m2.append(lst[i])
for i in range(n):
    res = [0 for index in range(n)]
    for j in range(n):
        for k in range(n):
            res[j] += m1[i][k] * m2[k][j]
    print(*(elem for elem in res), sep=",", end="")
    print()

