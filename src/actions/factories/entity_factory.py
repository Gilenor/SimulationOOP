from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Type

import config
from src.entities import Grass, Herbivore, Predator, Rock, Tree

if TYPE_CHECKING:
    from src.entities.entity import Entity


class EntityFactory(ABC):
    _INIT_PARAMS = {}

    @abstractmethod
    def __init__(self, entity_type: Type["Entity"]):
        self._create_type = entity_type

    def __call__(self, *args, **kwargs) -> "Entity":
        kwargs = {**self._INIT_PARAMS, **kwargs}
        return self._create_type(*args, **kwargs)

    @property
    def entity_type(self) -> Type["Entity"]:
        return self._create_type


class RockFactory(EntityFactory):
    def __init__(self, entity_type=Rock):
        super().__init__(entity_type)


class TreeFactory(EntityFactory):
    def __init__(self, entity_type=Tree):
        super().__init__(entity_type)


class GrassFactory(EntityFactory):
    def __init__(self, entity_type=Grass):
        super().__init__(entity_type)


class HerbivoreFactory(EntityFactory):
    _INIT_PARAMS = {"speed": config.HERBIVORE.speed, "health": config.HERBIVORE.health}

    def __init__(self, entity_type=Herbivore):
        super().__init__(entity_type)


class PredatorFactory(EntityFactory):
    _INIT_PARAMS = {
        "speed": config.PREDATOR.speed,
        "attack": config.PREDATOR.attack,
        "health": config.PREDATOR.health,
    }

    def __init__(self, entity_type=Predator):
        super().__init__(entity_type)
