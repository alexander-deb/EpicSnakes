from Field import Field
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __bool__(self):
        first =  False if self.x < 0 or self.y < 0 else True
        second = False if self.x >= Field.field_size or self.y >= Field.field_size else True
        return first and second
    
    def __hash__(self):
        return hash((self.x, self.y))
