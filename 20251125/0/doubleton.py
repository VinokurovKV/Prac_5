class Doubleton(type):
    _instance = []
    _count = 1
    def __call__(cls, *args, **kw):
        if len(cls._instance) < 2:
            cls._instance.append(super().__call__(*args, **kw))
        cls._count = 1-cls._count;
        return cls._instance[cls._count]

class C(metaclass=Doubleton): pass
print(*(C() for i in range(7)), sep="\n")
