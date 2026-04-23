from abc import ABC, abstractmethod
from typing import Dict, Type

from config import CONSOLE_TEXT_SPRITES
from src.entities.entity import Entity

from .sprite import ConsoleTextSprite, Sprite


class SpriteMap(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_sprite(self, entity: Entity) -> Sprite:
        pass


class ConsoleSpriteMap(SpriteMap):
    def __init__(self):
        super().__init__()

    def get_sprite(self, entity: Entity) -> Sprite:
        return super().get_sprite(entity)


class ConsoleTextSpriteMap(SpriteMap):
    def __init__(self):
        self._sprite_map: Dict[Type[Entity], str] = CONSOLE_TEXT_SPRITES

    def get_sprite(self, entity: Entity) -> Sprite:
        # WARNING: возможно получать спрайт по типу класса не лучшая идея
        data = self._sprite_map.get(type(entity))

        return ConsoleTextSprite(data)
