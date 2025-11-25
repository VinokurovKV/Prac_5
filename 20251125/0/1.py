A = type("A", (), {"value": 1234, "getvalue": lambda self: self.value})
a = A()
print(a.value, a.getvalue())
