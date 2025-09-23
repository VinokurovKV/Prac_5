lst = list(eval(input()))
key_lst = []
for x in lst:
    key_lst.append(x*x % 100)

for i in range(len(lst)):    
    for j in range(i + 1, len(key_lst)):
        if key_lst[i] > key_lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print(lst)
