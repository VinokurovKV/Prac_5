def average(a, *args):
    return sum([a, *args]) / (len(args) + 1)
l = eval(input())
print(average(10, l))
    
