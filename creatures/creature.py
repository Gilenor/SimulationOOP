from entities import Entity
from abc import abstractmethod


class Creature(Entity):
    @abstractmethod
    def __init__(self, health: int, speed: int):
        self.health = health
        self.speed = speed

    @abstractmethod
    def make_move(self):
        pass
