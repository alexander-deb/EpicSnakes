from Point import Point
from abc import ABC, abstractmethod
from random import choice
import Globals


class SnakeStrategy(ABC):
    '''
    Abstract class for Strategy pattern
    '''
    @abstractmethod
    def next_position(self, snake):
        '''
        Calculates next position of the Snake
        '''
        pass


class RandomStrategy(SnakeStrategy):
    '''
    Strategy class. Chooses random direction for every step of Snake
    '''

    def next_position(self, snake):

        directions = []
        for direct in Globals.directions:
            if direct + snake.coordinates[0]:
                directions.append(direct)
        directions.remove(snake.coordinates[1] - snake.coordinates[0])

        snake.direction = choice(directions)

        snake.coordinates.appendleft(snake.coordinates[0] + snake.direction)
        if not snake.tail:
            del snake.coordinates[-1]
        else:
            snake.tail = False


class DirectStrategy(SnakeStrategy):
    '''
    Strategy class. Chooses random Point in field and moves snke to it (first on X axis, then on Y)
    '''

    def next_position(self, snake):
        if not snake.goal:
            snake.change_goal()
        flag = True
        while flag:
            dx = snake.goal.x - snake.coordinates[0].x
            dy = 0
            if dx:
                dx = dx // abs(dx)
                flag = False
            else:
                dy = snake.goal.y - snake.coordinates[0].y
                if dy:
                    dy = dy // abs(dy)
                    flag = False
                else:
                    snake.change_goal()
        snake.direction = Point(dx, dy)
        snake.coordinates.appendleft(snake.coordinates[0] + snake.direction)
        if not snake.tail:
            del snake.coordinates[-1]
        else:
            snake.tail = False
