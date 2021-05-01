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
            field[fruit.coordinates.x][fruit.coordinates.y] = "F"
        for snake in self.snakes:
            for coordinate in snake.coordinates:
                field[coordinate.x][coordinate.y] = "S"

        for i in range(Globals.field_size):
            print(*field[i])

    def run(self):
        fruit = generate_fruit("Pineapple", Point(2,1))
        self.fruits.append(fruit)
        snake = Snake([Point(1, 1), Point(1,2), Point(2,2)], "red")
        self.snakes.append(snake)
        while True:
            self.display_objects()
            for snake in self.snakes:
                snake.next_position()
                i = 0
                while i < len(self.fruits):
                    if snake.coordinates[0] == self.fruits[i].coordinates:
                        snake.take_bonus(self.fruits[i])
                        self.fruits.pop(i)
                    else:
                        i += 1

            sleep(0.2)
            os.system("clear")
            

