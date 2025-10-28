class Rectangle:
    rectcnt = 0
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.__class__.rectcnt += 1
        setattr(self, f"rect_{self.rectcnt}", self.rectcnt)
    def __str__(self):
        return f"({self.x1}, {self.y1})({self.x1}, {self.y2})({self.x2}, {self.y2})({self.x2}, {self.y1}), {self__class__.rectcnt}"


