n = int(input())
end = n + 2
i = n
if n > 0:
    while i <= end:
        j = n
        while j <= end:
            p = i * j
            s = 0
            while p != 0:
                s += p % 10
                p //= 10
            if s == 6:
                print(i, "*", j, "=", ":=)", end=" ")
            else:
                print(i, "*", j, "=", i * j, end=" ")
            j += 1
        print(end="\n")
        i += 1
