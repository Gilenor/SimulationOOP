from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import config
from src.entities import Grass, Herbivore, Predator, Rock, Tree

if TYPE_CHECKING:
    from src.entities import Entity


class EntityFactory(ABC):
    @abstractmethod
    def __call__(self, *args, **kwds) -> "Entity":
        pass


class RockFactory(EntityFactory):
    def __call__(self, *args, **kwds) -> "Entity":
        return Rock()


class TreeFactory(EntityFactory):
    def __call__(self, *args, **kwds) -> "Entity":
        return Tree()


class GrassFactory(EntityFactory):
    def __call__(self, *args, **kwds) -> "Entity":
        return Grass()


class HerbivoreFactory(EntityFactory):
    __INIT_PARAMS = {
        "speed": config.HERBIVORE.speed,
        "health": config.HERBIVORE.health
    }

    def __call__(self, *args, **kwds) -> "Entity":
        return Herbivore(**self.__INIT_PARAMS)


class PredatorFactory(EntityFactory):
    __INIT_PARAMS = {
        "speed": config.PREDATOR.speed,
        "attack": config.PREDATOR.attack,
        "health": config.PREDATOR.health
    }

    def __call__(self, *args, **kwds) -> "Entity":
        return Predator(**self.__INIT_PARAMS)
