s = input().lower()
count = 0
arr = []
for i in range(len(s) - 1):
    if s[i].isalpha() and s[i + 1].isalpha():
        tmp = ""
        tmp += s[i] + s[i + 1]
        if tmp not in arr:
            arr.append(tmp)
            count += 1

print(count)
