match eval(input()):
    case "QWE":
        print("QWE!")
    case int(n):
        print("Int:", n)
    case (0, *tail):
        print("Zero tuple", tail)
    case _:
        print("UNKNOWN")

