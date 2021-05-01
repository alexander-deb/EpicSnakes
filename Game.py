import os

from time import sleep
from FruitFactory import generate_fruit
from Globals import Globals
from Point import Point
from random import randint, choice
from SnakePrototype import Snake
import copy

class Game:
    def __init__(self):
        self.weapon = "finger"
        self.score = 0
        self.name = input("Enter your name: ")
        self.snakes = []
        self.fruits = []
        
    def display_objects(self):
        field = [["_"]*Globals.field_size for i in range(Globals.field_size)]
        for fruit in self.fruits:
            field[fruit.coordinates.x][fruit.coordinates.y] = "F"
        for snake in self.snakes:
            for coordinate in snake.coordinates:
                field[coordinate.x][coordinate.y] = "S"

        for i in range(Globals.field_size):
            print(*field[i])

    def run(self):
        self.fruits.append(generate_fruit(choice(Globals.fruits)))
        self.fruits.append(generate_fruit(choice(Globals.fruits)))

        self.fruits.append(generate_fruit(choice(Globals.fruits)))

        snake = Snake([Point(1, 1), Point(1,2), Point(2,2)], "red")
        self.snakes.append(snake)
        self.snakes.append(Snake([Point(5, 1), Point(5,2), Point(6,2)], "red"))

        while True:
            self.display_objects()
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

            sleep(0.1)
            os.system("clear")
            

