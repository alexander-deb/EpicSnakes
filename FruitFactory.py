from __future__ import annotations
from abc import ABC, abstractmethod
from Point import Point
from random import randint
from Field import Field


class FruitCreator(ABC):
    '''
    Abstract actory for pattern
    '''
    @abstractmethod
    def factory_method(self):
        pass

    def create(self, coordinates):
        '''
        Creates fruit on coordinates
        '''
        fruit = self.factory_method(coordinates)
        return fruit


class AppleCreator(FruitCreator):
    '''
    Creator class for Apples
    '''

    def factory_method(self, coordinates):
        return Apple(coordinates)


class PineappleCreator(FruitCreator):
    '''
    Creator class for Pineapples
    '''

    def factory_method(self, coordinates):
        return Pineapple(coordinates)


class Fruit(ABC):
    '''
    Abstract class for fruits
    '''
    @abstractmethod
    def __str__(self):
        pass


class Apple():
    '''
    Class for Apples.
    Apple gives an extra point to Snakes tail.
    '''

    def __init__(self, coordinates):
        self.color = "red"
        self.coordinates = coordinates

    def __str__(self):
        return "Apple"


class Pineapple():
    '''
    Class for Pinepples.
    Pineapple clones a Snake. If Snake eats Pineapple, amount of Snakes will increase.
    '''

    def __init__(self, coordinates):
        self.color = "yellow"
        self.coordinates = coordinates

    def __str__(self):
        return "Pineapple"


def generate_fruit(fruit):
    '''
    Factory method to generate new fruit on random Point
    '''
    coordinates = Point(randint(0, Field.field_size-1),
                        randint(0, Field.field_size-1))
    if fruit == "Apple":
        return AppleCreator().create(coordinates)
    elif fruit == "Pineapple":
        return PineappleCreator().create(coordinates)
