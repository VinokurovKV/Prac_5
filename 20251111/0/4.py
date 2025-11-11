class Sender:
  f = True
  @classmethod
  def report(self):
    if self.f:
      print("Greetings!")
      self.f = False
    else:
      print("Get away!")

class Asker:
  @staticmethod
  def askall(lst):
    for i in lst:
      i.report()

a = [Sender(), Sender(), Sender()]

Asker.askall(a)