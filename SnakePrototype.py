import copy

from Globals import Globals
from Point import Point
from random import randint, choice
from collections import deque

class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class Snake:
    def __init__(self, coordinates, color):
        self.coordinates = deque(coordinates)
        self.direction = None
        self.color = color
        print("Created Snake")

    def next_position(self):
        directions = []
        for direct in Globals.directions:
            if direct + self.coordinates[0]:
                directions.append(direct)
        directions.remove(self.coordinates[1] - self.coordinates[0])

        self.direction = choice(directions)

        self.coordinates.appendleft(self.coordinates[0] + self.direction)
        del self.coordinates[-1] 


    def __copy__(self):
        coordinates = copy.copy(self.coordinates)
        new = self.__class__(
            coordinates, self.direction, self.color
        )
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo={}):
        # First, let's create copies of the nested objects.
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        coordinates = copy.deepcopy(self.coordinates, memo)
        new = self.__class__(
            coordinates, self.direction, self.color
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new


if __name__ == "__main__":
    snake = Snake([Point(1, 1), Point(1,2), Point(2,2)], "red")
    snake.next_position()
    print(snake.coordinates)
    