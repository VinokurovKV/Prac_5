n = int(input())
if n % 2 == 0:
    if n % 25 == 0 and n % 8 == 0:
        print("A + B - C +")
    elif n % 25 == 0:
        print("A + B - C -")
    elif n % 8 == 0:
        print("A - B - C +")
    else:
        print("A - B - C -")
else:
    if n % 25 == 0:
        print("A - B + C -")
    else:
        print("A - B - C -")

