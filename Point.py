from Field import Field


class Point:
    '''
    My own type of data. Acts like a vector
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        '''
        returns representation of point
        '''
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        '''
        returns new point (x1 + y1, x2 + y2)
        '''
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        '''
        returns new point (x1 - y1, x2 - y2)
        '''
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __eq__(self, other):
        '''
        returns bool eq or neq
        '''
        return self.x == other.x and self.y == other.y

    def __bool__(self):
        '''
        returns bool (is in field or not)
        '''
        is_in_field_left = False if self.x < 0 or self.y < 0 else True
        is_in_field_right = False if self.x >= Field.field_size or self.y >= Field.field_size else True
        return is_in_field_left and is_in_field_right

    def __hash__(self):
        '''
        returns hash like a tuple
        '''
        return hash((self.x, self.y))
