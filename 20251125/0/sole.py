class sole(type):
    def __new__(metacls, name, parents, ns):
        if len(parents) != 1:
            raise TypeError
        return super().__new__(metacls, name, parents, ns)

