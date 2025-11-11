from collections import UserString

class DivStr(UserString):
  def __init__(self, seq=''):
    super().__init__(seq)

  def __floordiv__(self, n):
    length = len(self.data)
    iterator = length // n
    iter_seq = []
    for i in range(n):
      iter_seq.append(self.__class__(self.data[i * iterator:(i + 1) * iterator]))
    return iter(iter_seq)
  
  def __mod__(self, n):
    length = len(self.data)
    remainder = length % n

    return self.__class__(self.data[-remainder:] if remainder != 0 else "")
  
import sys
exec(sys.stdin.read())