import copy

from Globals import Globals
from Point import Point
from random import randint, choice
from collections import deque
from abc import ABC, abstractmethod
from Strategy import DirectStrategy, RandomStrategy


class Snake:
    '''
    class for Snakes using Prortotype and Strategy patterns
    '''
    def __init__(self, coordinates, color):
        self.coordinates = deque(coordinates)
        self.direction = None
        self.color = color
        self.tail = False
        self.strategy = RandomStrategy()
        self.goal = None

    def next_position(self):
        '''
        calculates next position of snake
        '''
        self.strategy.next_position(self)
    
    def take_bonus(self):
        '''
        is necessary to add new element on tail?
        '''
        self.tail = True

    def change_goal(self):
        '''
        calculates new goal in field
        '''
        self.goal = Point(randint(0, Globals.field_size-1), randint(0, Globals.field_size-1))


    def __copy__(self):
        '''
        method for copy.copy()
        '''
        coordinates = copy.copy(self.coordinates)
        new = self.__class__(
            coordinates, self.color
        )
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo={}):
        '''
        method for copy.deepcopy()
        '''
        # First, let's create copies of the nested objects.
        coordinates = copy.deepcopy(self.coordinates, memo)
        new = self.__class__(
            coordinates, self.color
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new


if __name__ == "__main__":
    snake = Snake([Point(1, 1), Point(1,2), Point(2,2)], "red")
    snake.change_goal()
    print(snake.goal)
    for i in range(10):
        snake.next_position()
        print(snake.coordinates)
        