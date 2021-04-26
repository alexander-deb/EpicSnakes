from FruitFactory import generate_fruit
from SnakePrototype import Snake

class Game:
    def __init__(self, ):
        self.weapon = "finger"
        self.score = 0
        self.name = input("Enter your name: ")
        
    
    def run():
        fruit = generate_fruit("Apple", (1,1))
        snake = Snake((1, 1), 1, "red")
        print(fruit.give_bonus())
        print(fruit.coordinates)

