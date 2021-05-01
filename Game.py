import os

from time import sleep
from FruitFactory import generate_fruit
from Globals import Globals
from Point import Point
from random import randint
from SnakePrototype import Snake

class Game:
    def __init__(self):
        self.weapon = "finger"
        self.score = 0
        self.name = input("Enter your name: ")
        self.snakes = []
        self.fruits = []
        
    def display_objects(self):
        field = [[0]*Globals.field_size for i in range(Globals.field_size)]
        for fruit in self.fruits:
            field[fruit.coordinates[0]][fruit.coordinates[1]] = "F"
        for snake in self.snakes:
            for coordinate in snake.coordinates:
                field[coordinate.x][coordinate.y] = "S"

        for i in range(Globals.field_size):
            print(*field[i])

    def run(self):
        fruit = generate_fruit("Apple", (1,5))
        self.fruits.append(fruit)
        snake = Snake([Point(1, 1), Point(1,2), Point(2,2)], "red")
        self.snakes.append(snake)
        while True:
            self.display_objects()
            for snake in self.snakes:
                snake.next_position()
            sleep(0.1)
            os.system("clear")
            

