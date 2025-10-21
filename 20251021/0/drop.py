from itertools import dropwhile
from itertools import islice, count

def genf():
    s = 0
    for i in count(1):
        s += 1 / (i * i)
        yield s

print(list(islice(dropwhile(lambda x: x < 1.6, genf()), 10)))
