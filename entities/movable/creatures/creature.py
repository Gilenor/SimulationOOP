from ..moving_entity import Movable
from abc import abstractmethod, abstractproperty


class Creature(Movable):
    @abstractmethod
    def __init__(self, health: int, speed: int):
        self.health = health
        self.speed = speed
