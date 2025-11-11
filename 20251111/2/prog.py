class Num:
  def __init__(self):
    self.values = {}
    
  def __get__(self, instance, owner):
    if instance is None:
      return self
    return self.values.get(id(instance), 0)
    
  def __set__(self, instance, value):
    if hasattr(value, 'real'):
      self.values[id(instance)] = value.real
    elif hasattr(value, '__len__'):
      self.values[id(instance)] = len(value)

import sys
exec(sys.stdin.read())