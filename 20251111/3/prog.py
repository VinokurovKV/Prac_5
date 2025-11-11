class Vowel:
  __slots__ = ['a', 'e', 'i', 'o', 'u', 'y', 'full']
  _vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
  
  def __init__(self, **kwargs):
    for vowel in self._vowels:
        object.__setattr__(self, vowel, None)
    object.__setattr__(self, 'full', False)
    
    for key, value in kwargs.items():
        if key in self._vowels:
            object.__setattr__(self, key, value)
    
    self._update_full()
  
  def _update_full(self):
    full_status = all(object.__getattribute__(self, vowel) is not None for vowel in self._vowels)
    object.__setattr__(self, 'full', full_status)
  
  @property
  def answer(self):
    return 42
  
  def __setattr__(self, name, value):
    if name == 'answer':
        raise AttributeError("Cannot set attribute 'answer'")
    elif name not in self.__slots__:
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    elif name in self._vowels:
        object.__setattr__(self, name, value)
        self._update_full()
    elif name == 'full':
        pass
    else:
        object.__setattr__(self, name, value)
  
  def __getattribute__(self, name):
    if name in Vowel._vowels: 
        value = object.__getattribute__(self, name)
        if value is None:
            raise AttributeError(f"Vowel '{name}' not set")
        return value
    return object.__getattribute__(self, name)
  
  def __str__(self):
    parts = []
    for vowel in sorted(Vowel._vowels):
        value = object.__getattribute__(self, vowel)
        if value is not None:
            parts.append(f"{vowel}: {value}")
    return ", ".join(parts)
    
import sys
exec(sys.stdin.read())