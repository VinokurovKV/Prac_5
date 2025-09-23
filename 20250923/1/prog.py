m, n = eval(input())
print(list([i for i in range(m, n) if all([i % j for j in range(2, i // 2 + 1)])]))
