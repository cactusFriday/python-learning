

class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._full_name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val
        self._full_name = None
    
    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, val):
        self._surname = val
        self._full_name = None
    
from time import time
from random import choice

# Non data desc for class MyTime
class Epoch:
    def __get__(self, instanse, owner_class):
        return int(time())

class MyTime:
    epoch = Epoch()

m = MyTime()

class Dice:
    @property
    def number(self):
        return choice(range(1, 7))

# Код делает одно и то же - дергает random element from iterable :: (not DRY)
# class Game:
#     @property
#     def rock_paper_scissors(self):
#         return choice(['Rock', 'Paper', 'Scissors'])

#     @property
#     def coin_toss(self):
#         return choice(['Heads', 'Tails'])
    
#     @property
#     def dice(self):
#         return choice(range(1, 7))

# Non data descriptor for class Game
class Choice:
    def __init__(self, *args) -> None:
        self._choice = args
    
    def __get__(self, instance, owner):
        return choice(self._choice)

class Game:
    dice = Choice(1, 2, 3, 4, 5, 6)
    toss_coin = Choice('Heads', 'Tails')
    rock_paper_scissors = Choice('Rock', 'Paper', 'Scissors')


d = Game()