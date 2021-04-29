from __future__ import annotations
from abc import ABC, abstractmethod


class FruitCreator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def create(self, coordinates):
        fruit = self.factory_method(coordinates)
        return fruit


class AppleCreator(FruitCreator):
    def factory_method(self, coordinates):
        return Apple(coordinates)


class PineappleCreator(FruitCreator):
    def factory_method(self, coordinates):
        return Pineapple(coordinates)


class Fruit(ABC):
    @abstractmethod
    def give_bonus(self):
        pass

class Apple(Fruit):
    def __init__(self, coordinates):
        self.color = "red"
        self.coordinates = coordinates
        self.bonus = 2

    def give_bonus(self):
        return self.bonus

class Pineapple(Fruit):
    def __init__(self, coordinates):
        self.color = "red"
        self.coordinates = coordinates
        self.bonus = -2

    def give_bonus(self):
        return self.bonus

def generate_fruit(fruit, coordinates):
    if fruit == "Apple":
        print("Created Apple")
        return AppleCreator().create(coordinates)
    elif fruit == "Pineapple":
        print("Created Pinepple")
        return PineappleCreator().create(coordinates)
