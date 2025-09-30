lst = eval(input())
print(sorted(lst, key=lambda x: x * x % 100))
