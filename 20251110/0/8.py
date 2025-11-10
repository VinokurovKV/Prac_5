def div(a, b, eps):
    if b < eps:
        raise ZeroDivisionError
    return a / b

print(div(2, 5, 1))
print(div(3, 4, 4))
print(div(5, 5, 10))
print(div(5, 0, 1))

