a, b = eval(input())
for n in range(a, b + 1):
    if '3' not in str(n):
        print(n)
lst = [i for i in range(a, b + 1) if '3' not in str(i)]
print(lst)

