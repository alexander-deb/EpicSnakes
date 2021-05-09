from FruitFactory import generate_fruit
from Globals import Globals
from Field import Field
from Point import Point
from random import choice
from SnakePrototype import Snake
import copy


class Game:
    '''
    Main game class
    '''

    def __init__(self):
        self.weapon = "finger"
        self.score = 0
        self.name = "Alex"
        self.snakes = []
        self.fruits = []

    def display_objects(self):
        '''
        Displays field filled with objects
        '''
        field = [["_"]*Field.field_size for i in range(Field.field_size)]
        for fruit in self.fruits:
            field[fruit.coordinates.x][fruit.coordinates.y] = "F"
        for snake in self.snakes:
            for coordinate in snake.coordinates:
                field[coordinate.x][coordinate.y] = "S"

        for i in range(Field.field_size):
            print(*field[i])

    def choose_difficulty(self, difficulty):
        '''
        Changes the difficulty. 
        P.S. depends on user click in GUI
        '''
        self.difficulty = difficulty
        if self.difficulty == 1:
            Field.field_size = 10
            Globals.display_delay = 300
            Globals.snakes_quantity = 2
            Globals.fruits_quantity = 2
        elif self.difficulty == 2:
            Field.field_size = 20
            Globals.display_delay = 150
            Globals.snakes_quantity = 4
            Globals.fruits_quantity = 4
        elif self.difficulty == 3:
            Field.field_size = 30
            Globals.display_delay = 75
            Globals.snakes_quantity = 10
            Globals.fruits_quantity = 5
        self.create_objects()

    def create_objects(self):
        '''
        Generates first Fruits and Snakes
        '''
        start_point = Field.field_size // 2
        for i in range(Globals.fruits_quantity):
            self.fruits.append(generate_fruit(choice(Globals.fruits)))
        snake = Snake([Point(start_point, start_point), Point(
            start_point, start_point+1), Point(start_point+1, start_point+1)], "blue")
        for i in range(Globals.snakes_quantity):
            self.snakes.append(copy.deepcopy(snake))

    def run(self):
        '''
        Main function. Calculates every frame of the Game.
        '''
        for snake in self.snakes:
            snake.next_position()
            i = 0
            while i < len(self.fruits):
                if snake.coordinates[0] == self.fruits[i].coordinates:
                    if str(self.fruits[i]) == "Apple":
                        self.snakes.append(copy.deepcopy(snake))
                    elif str(self.fruits[i]) == "Pineapple":
                        snake.take_bonus()
                    self.fruits.pop(i)
                    self.fruits.append(generate_fruit(choice(Globals.fruits)))

                else:
                    i += 1
