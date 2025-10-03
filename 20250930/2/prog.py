def type_diff(a, b):
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        res = []
        for i in a:
            if i not in b:
                res.append(i)
        if isinstance(a, list) and isinstance(b, list):
            return list(res)
        elif isinstance(a, tuple) and isinstance(b, tuple):
            return tuple(res)
        else:
            print("Wrong types!")
            return
    else:
        return a - b

l = eval(input())
print(type_diff(*l))
