from .world import World

from typing import TYPE_CHECKING, List, Dict, Tuple

if TYPE_CHECKING:
    from entities import Entity
    from position import Position


class World2D(World):
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._entities: Dict['Position', 'Entity'] = {}

    def add_entity(self, entity: 'Entity', position: 'Position'):
        if position not in self._entities:
            self._entities[position] = entity
        else:
            raise KeyError(f"This position: {position.get_coords()} was busy")

    def remove_entity(self, entity: 'Entity'):
        position = None
        for p, e in self._entities.items():
            if entity == e:
                position = p
                break

        if position:
            del self._entities[position]

    def get_entities(self) -> List['Entity']:
        return list(self._entities.values())

    def get_entity_position(self, entity: 'Entity') -> 'Position':
        for pos, e in self._entities.items():
            if entity == e:
                return pos
        raise Exception("Entity was not found in world!")

    def get_dimensions(self) -> Tuple:
        return (self._width, self._height)
