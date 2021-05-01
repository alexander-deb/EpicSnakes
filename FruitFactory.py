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
    def __str__(self):
        pass

class Apple():
    def __init__(self, coordinates):
        self.color = "red"
        self.coordinates = coordinates

    def __str__(self):
        return "Apple"

class Pineapple():
    def __init__(self, coordinates):
        self.color = "yellow"
        self.coordinates = coordinates

    def __str__(self):
        return "Pineapple"

def generate_fruit(fruit, coordinates):
    if fruit == "Apple":
        print("Created Apple")
        return AppleCreator().create(coordinates)
    elif fruit == "Pineapple":
        print("Created Pinepple")
        return PineappleCreator().create(coordinates)
