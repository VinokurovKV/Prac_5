class Maze:
    def __init__(self, N):
        self.size = N
        self.connections = {}
        for i in range(N):
            for j in range(N):
                self.connections[(i, j)] = set()
    
    def __setitem__(self, key, value):
        x1, y1, x2, y2 = key[0], key[1].start, key[1].stop, key[2]
        
        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2)):
                if value == "·":
                    self.connections[(x1, j)].add((x1, j+1))
                    self.connections[(x1, j+1)].add((x1, j))
                elif value == "█":
                    self.connections[(x1, j)].discard((x1, j+1))
                    self.connections[(x1, j+1)].discard((x1, j))
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)):
                if value == "·":
                    self.connections[(i, y1)].add((i+1, y1))
                    self.connections[(i+1, y1)].add((i, y1))
                elif value == "█":
                    self.connections[(i, y1)].discard((i+1, y1))
                    self.connections[(i+1, y1)].discard((i, y1))
    
    def __getitem__(self, key):
        x1, y1, x2, y2 = key[0], key[1].start, key[1].stop, key[2]
        
        visited = set()
        queue = [(x1, y1)]
        visited.add((x1, y1))
        
        while queue:
            x, y = queue.pop(0)
            if (x, y) == (x2, y2):
                return True
            for neighbor in self.connections[(x, y)]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False
    
    def __str__(self):
        field = [["█"] * (2*self.size+1) for _ in range(2*self.size+1)]
        for i in range(self.size):
            for j in range(self.size):
                field[1 + 2*j][1 + 2*i] = "·"
                for dx, dy in self.connections[(i, j)]:
                    field[1 + 2*j + (dy - j)][1 + 2*i + (dx - i)] = "·"
        return "\n".join("".join(row) for row in field)
    
import sys
exec(sys.stdin.read())