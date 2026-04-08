from abc import ABC, abstractmethod
from config import CONSOLE_TEXT_SPRITES
from entities import Empty
from .sprite import ConsoleSprite, ConsoleTextSprite

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .sprite import Sprite
    from entities import Entity


class SpriteMap(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_sprite(self, sprite_type: 'Entity') -> 'Sprite':
        pass

    @abstractmethod
    def get_empty_sprite(self) -> 'Sprite':
        pass


class ConsoleSpriteMap(SpriteMap):
    def __init__(self):
        super().__init__()

    def get_sprite(self, sprite_type: 'Entity') -> 'Sprite':
        return super().get_sprite(sprite_type)

    def get_empty_sprite(self) -> 'Sprite':
        return super().get_empty_sprite()


class ConsoleTextSpriteMap(SpriteMap):
    def __init__(self):
        self._sprite_map = CONSOLE_TEXT_SPRITES

    def get_sprite(self, entity: 'Entity') -> 'Sprite':
        # WARNING: возможно получать спрайт по имени класса не лучшая идея
        data = self._sprite_map.get(str(entity))

        return ConsoleTextSprite(data)

    def get_empty_sprite(self) -> 'Sprite':
        return self.get_sprite(Empty())
