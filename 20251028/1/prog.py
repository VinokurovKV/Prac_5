class Omnibus:
    _attrs = {}
    _instances = set()

    def __init__(self):
        self._id = id(self)
        Omnibus._instances.add(self._id)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            if not hasattr(self, '_attrs_tracker'):
                self._attrs_tracker = set()
            if name not in self._attrs_tracker:
                self._attrs_tracker.add(name)
                if name in Omnibus._attrs:
                    Omnibus._attrs[name] += 1
                else:
                    Omnibus._attrs[name] = 1

    def __getattr__(self, name):
        if not name.startswith('_'):
            if name in Omnibus._attrs:
                return Omnibus._attrs[name]
        raise AttributeError()

    def __delattr__(self, name):
        if not name.startswith('_'):
            if hasattr(self, '_attrs_tracker') and name in self._attrs_tracker:
                self._attrs_tracker.remove(name)
                if name in Omnibus._attrs:
                    Omnibus._attrs[name] -= 1
                    if Omnibus._attrs[name] == 0:
                        del Omnibus._attrs[name]

import sys
exec(sys.stdin.read())