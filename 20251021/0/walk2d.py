def walk2d():
    x, y = 0, 0
    while True:
        dx, dy = yield x, y
        x += dx
        y += dy


g = walk2d()
next(g)
g.send((1, 1))
g.send((3, -4))
