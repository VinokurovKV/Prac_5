def itemget(collection, index):
    return collection[index]

def safeindex(function, *args):
    try:
        return function(*args)
    except IndexError:
        return None

print(list(safeindex(itemget, "qwe", i) for i in range(5)))
print(safeindex(itemget, "qwe", "qwe"))

