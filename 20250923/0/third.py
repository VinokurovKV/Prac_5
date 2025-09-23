l = eval(input())
count = 0
half = []
for i in l:
    count += 1
if count % 2 != 0:
    print("Oops!")
else:
    sliced = count // 2 - 1
    half += l[-1:sliced:-2]
    print(half)

