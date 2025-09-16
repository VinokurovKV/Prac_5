match n := int(input()):
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case a if a % 2 != 0:
        print(a, "is many")
    case _:
        print("Even many")
