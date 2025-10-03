def Pareto(*args):
    pare = []
    for i in args:
        if all(not (i[0] <= j[0] and i[1] <= j[1] and i[0] < j[0] and i[1] < j[1]) for j in args):
            pare.append(i)
    return tuple(pare)

l = eval(input())
print(Pareto(*l))
