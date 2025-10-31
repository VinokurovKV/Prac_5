class Triangle:
    def __init__(self, a, b, c):
        self.a = tuple(a)
        self.b = tuple(b)
        self.c = tuple(c)
    
    def __abs__(self):
        x1, y1 = self.a
        x2, y2 = self.b
        x3, y3 = self.c
        area = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
        if not area:
            return 0
        return area
    
    def __bool__(self):
        return abs(self) > 1e-12
    
    def __lt__(self, other):
        return abs(self) < abs(other)
    
    def _point_in_triangle(self, p, tri):
        def sign(p1, p2, p3):
            return (p1[0]-p3[0])*(p2[1]-p3[1]) - (p2[0]-p3[0])*(p1[1]-p3[1])
        
        a, b, c = tri.a, tri.b, tri.c
        d1 = sign(p, a, b)
        d2 = sign(p, b, c)
        d3 = sign(p, c, a)
        
        has_neg = (d1 < -1e-12) or (d2 < -1e-12) or (d3 < -1e-12)
        has_pos = (d1 > 1e-12) or (d2 > 1e-12) or (d3 > 1e-12)
        
        return not (has_neg and has_pos)
    
    def __contains__(self, other):
        if not bool(other):
            return True
        if not bool(self):
            return False
        return (self._point_in_triangle(other.a, self) and 
                self._point_in_triangle(other.b, self) and 
                self._point_in_triangle(other.c, self))
    
    def _segments_intersect(self, p1, p2, p3, p4):
        def orientation(p, q, r):
            val = (q[1]-p[1])*(r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])
            if abs(val) < 1e-12: return 0
            return 1 if val > 0 else 2
        
        def on_segment(p, q, r):
            return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
                    min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))
        
        o1 = orientation(p1, p2, p3)
        o2 = orientation(p1, p2, p4)
        o3 = orientation(p3, p4, p1)
        o4 = orientation(p3, p4, p2)
        
        if o1 != o2 and o3 != o4:
            return True
        
        if o1 == 0 and on_segment(p1, p3, p2): return True
        if o2 == 0 and on_segment(p1, p4, p2): return True
        if o3 == 0 and on_segment(p3, p1, p4): return True
        if o4 == 0 and on_segment(p3, p2, p4): return True
        
        return False
    
    def __and__(self, other):
        if not bool(self) or not bool(other):
            return False
        
        for tri1, tri2 in [(self, other), (other, self)]:
            for p in [tri1.a, tri1.b, tri1.c]:
                if tri2._point_in_triangle(p, tri2):
                    return True
        
        edges1 = [(self.a, self.b), (self.b, self.c), (self.c, self.a)]
        edges2 = [(other.a, other.b), (other.b, other.c), (other.c, other.a)]
        
        for e1 in edges1:
            for e2 in edges2:
                if self._segments_intersect(e1[0], e1[1], e2[0], e2[1]):
                    return True
        
        return False
    
import sys
exec(sys.stdin.read())