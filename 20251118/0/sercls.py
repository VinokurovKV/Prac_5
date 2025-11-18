import pickle

class SerCls:
    def __init__(self, l=None, d=None, n=None, s=None):
        self.lst = list(l)
        self.dct = dict(d)
        self.num = int(n)
        self.st = str(s)

    def __str__(self):
        return ' '.join([str(self.lst), str(self.dct), str(self.num), self.st])


ser = SerCls([1, 2, 3], {11: 27}, 10, '123456')
t = pickle.dumps(ser)
del ser
ser1 = pickle.loads(t)
print(ser1)
