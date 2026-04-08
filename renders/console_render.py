from .render import Render

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from worlds import World
    from entities import Entity
    from position import Position
    from sprites import SpriteMap


class ConsoleRender(Render):
    def __init__(self, sprite_map: 'SpriteMap'):
        self._sprite_map = sprite_map

    def render(self, world: 'World'):
        entities = world.get_entities()
        view = ConsoleView(self._sprite_map, *world.get_dimensions())

        for entity in entities:
            position = world.get_entity_position(entity)
            view.add_entity_to_view(entity, position)

        print(view)
        del view


class ConsoleView:
    def __init__(self, sprite_map: 'SpriteMap', width: int, height: int, *dimensions: List):
        self._sprite_map = sprite_map

        # возможно нужно добавить проверку что измерений только два
        # но пока логика не предусматривает больше, они просто игнорируются
        self._sprites = [
            [sprite_map.get_empty_sprite()] * width for _ in range(height)]

    def __str__(self) -> str:
        row_to_str = lambda row: "".join(map(str, row))
        rows = [row_to_str(row) for row in self._sprites]

        return "\n".join(rows)

    def add_entity_to_view(self, entity: 'Entity', position: 'Position'):
        # сущность будет просто добавляться на указанную позицию
        # если там уже была сущность, то новая будет добавляться поверх нее
        x, y = position.get_coords()
        sprite = self._sprite_map.get_sprite(entity)
        # WARNING: пока все текстовы/консольные спрайты шириной в один символ
        #          но если это измениться то будет ошибка!!!
        self._sprites[y][x] = sprite


# render = ConsoleRender()
