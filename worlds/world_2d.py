from .world import World
from position import Position

from typing import TYPE_CHECKING, List, Dict, Tuple, Type

if TYPE_CHECKING:
    from entities import Entity


class World2D(World):
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._entities: Dict['Position', 'Entity'] = {}

    def add_entity(self, entity: 'Entity', position: 'Position'):
        if not self._is_inside(position):
            raise ValueError("Position out of bounds")
        if not self._is_free(position):
            raise ValueError(f"Position: {position.get_coords()} was occupied")

        self._entities[position] = entity

    def remove_entity(self, entity: 'Entity'):
        for pos, e in self._entities.items():
            if entity == e:
                self._entities.pop(pos)
                break

    def get_entities(self, entity_type: Type | None = None) -> List['Entity']:
        entities = list(self._entities.values())

        if entity_type is None:
            return entities
        return [e for e in entities if isinstance(e, entity_type)]

    def get_entity_position(self, entity: 'Entity') -> 'Position':
        for pos, e in self._entities.items():
            if entity == e:
                return pos
        raise ValueError("Entity was not found in world!")

    def get_empty_positions(self) -> List['Position']:
        positions = [ceil for ceil in self._ceils()
                     if ceil not in self._entities]

        return positions

    def get_dimensions(self) -> Tuple:
        return (self._width, self._height)

    # ---------- private ------------------------------------------------------

    def _is_free(self, position: 'Position') -> bool:
        return position not in self._entities

    def _is_inside(self, position: 'Position') -> bool:
        return (0 <= position.x < self._width) and (0 <= position.y < self._height)

    def _ceils(self):
        for x in range(self._width):
            for y in range(self._height):
                yield Position(x, y)
