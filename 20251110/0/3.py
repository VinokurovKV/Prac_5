A = type('AA', (), {'a': 123, '__init__': lambda self, val: setattr(self.__class__, 'Q-Q!', val), '__str__': lambda self: f'{self.val}', 'Q-Q!': 123})

a = A(10)
print(A.__dict__["Q-Q!"])
