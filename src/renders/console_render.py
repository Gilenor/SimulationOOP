import os
import platform

from typing import List

from .render import Render
from .sprites import SpriteMap, ConsoleTextSprite

from src.worlds import World
from src.position import Position
from src.entities.entity import Entity


class ConsoleRender(Render):
    def __init__(self, sprite_map: SpriteMap):
        self._sprite_map = sprite_map

    def render(self, world: World):
        entities = world.get_entities()
        view = ConsoleView(self._sprite_map, *world.get_dimensions())

        for entity in entities:
            position = world.get_entity_position(entity)
            view.add_entity_to_view(entity, position)

        for line in view.data:
            print("     ", line)

        #print(self._push_right(view.data, 5))
        print()

    def clear(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')


class ConsoleView:
    _EMPTY_SPRITE = ConsoleTextSprite("-")

    def __init__(
        self, sprite_map: SpriteMap, width: int, height: int, *dimensions: List
    ):
        self._sprite_map = sprite_map
        # возможно в будущем проявятся какие-то ошибки 
        # из-за использования _EMPTY_SPRITE в одном экземляре
        self._sprites = [[self._EMPTY_SPRITE] * width for _ in range(height)]

    @property
    def data(self) -> List[str]:
        return self._to_sting()

    def add_entity_to_view(self, entity: Entity, position: Position):
        # сущность будет просто добавляться на указанную позицию
        # если там уже была сущность, то новая будет добавляться поверх нее
        x, y, *_ = position.get_coords()
        sprite = self._sprite_map.get_sprite(entity)
        # WARNING: пока все текстовы/консольные спрайты шириной в один символ
        #          но если это измениться то будет ошибка!!!
        self._sprites[y][x] = sprite

    def _to_sting(self) -> List[str]:
        row_to_str = lambda row: "".join(map(str, row))
        rows = [row_to_str(row) for row in self._sprites]

        return rows
