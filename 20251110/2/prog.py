import math

class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass

def triangleSquare(inStr):
    try:
        points = eval(inStr)
    except Exception:
        raise InvalidInput("Invalid input")
    
    try:
        (x1, y1), (x2, y2), (x3, y3) = points
        if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2, x3, y3]):
            raise InvalidInput("Invalid input")
    except (ValueError, TypeError):
        raise InvalidInput("Invalid input")
    
    try:
        a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
        c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    except TypeError:
        raise BadTriangle("Not a triangle")
    
    if a + b <= c or a + c <= b or b + c <= a or a == 0 or b == 0 or c == 0:
        raise BadTriangle("Not a triangle")
    
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    return area

while True:
    try:
        s = input().strip()
        if not s:
            break
        
        area = triangleSquare(s)
        print(f"{area:.2f}")
        
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    except EOFError:
        break