s = 0
while n := int(input()):
    s += n
    if n < 0:
        print(n)
        break
    if s > 21:
        print(s)
        break
else:
    print(n)
