from typing import Dict, List, Optional, Tuple, Type

from src.entities.entity import Entity
from src.position import Position

from .world import World


class World2D(World):
    def __init__(self, width: int, height: int):
        super().__init__()

        self._width = width
        self._height = height
        self._entities: Dict[Position, Entity] = {}

    def add_entity(self, entity: Entity, position: Position):
        if not self.is_valid(position):
            raise ValueError(f"[add_entity]: Position: ({position}) out of bounds")
        if not self.is_free(position):
            raise ValueError(f"[add_entity]: Position: ({position}) was occupied")

        self._entities[position] = entity

    def remove_entity(self, entity: Entity):
        # WARNING: нужно ли бросать исключение если entity не найдена?
        for pos, e in self._entities.items():
            if entity == e:
                self._entities.pop(pos)
                break

    def move_entity_to(self, entity: Entity, new_pos: Position):
        self.remove_entity(entity)
        self.add_entity(entity, new_pos)

    def get_entities(self, entity_type: Optional[Type[Entity]] = None) -> List[Entity]:
        entities = list(self._entities.values())

        if entity_type is None:
            return entities
        return [e for e in entities if isinstance(e, entity_type)]

    def get_entity_position(self, entity: Entity) -> Position:
        for pos, e in self._entities.items():
            if entity is e:
                return pos
        # WARNING: возможно лучше бросать исключение
        raise ValueError("[get_entity_position]: Entity was not found in world!")
        # return None

    def get_entity_at(self, position: Position) -> Entity:
        if position in self._entities:
            return self._entities[position]
        # WARNING: возможно лучше бросать исключение
        raise ValueError(
            f"[get_entity_at]: Entity by position: ({position}) was not found in world!"
        )
        # return None

    def get_empty_positions(self) -> List[Position]:
        positions = [ceil for ceil in self._ceils() if ceil not in self._entities]

        return positions

    def get_dimensions(self) -> Tuple[int, ...]:
        return (self._width, self._height)

    def is_free(self, position: Position) -> bool:
        return position not in self._entities

    def is_valid(self, position: Position) -> bool:
        return (0 <= position.x < self._width) and (0 <= position.y < self._height)

    def is_exist(self, entity: Entity) -> bool:
        try:
            self.get_entity_position(entity)
            return True
        except ValueError:
            return False

    # ---------- private ------------------------------------------------------

    def _ceils(self):
        for x in range(self._width):
            for y in range(self._height):
                yield Position(x, y)
