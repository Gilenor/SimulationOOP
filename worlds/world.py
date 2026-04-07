from abc import ABC, abstractmethod

from typing import TYPE_CHECKING, List, Dict, Tuple

if TYPE_CHECKING:
    from entity import Entity
    from position import Position


class World(ABC):
    @abstractmethod
    def __init__(self, width: int, height: int):
        self._entities: Dict['Position', 'Entity'] = {}

    @abstractmethod
    def add_entity(self, entity: 'Entity', position: 'Position'):
        pass

    @abstractmethod
    def remove_entity(self, entity: 'Entity'):
        pass

    @abstractmethod
    def get_entities(self) -> List['Entity']:
        pass

    @abstractmethod
    def get_entity_position(self, entity: 'Entity') -> 'Position':
        pass

    @abstractmethod
    def get_dimensions(self) -> Tuple:
        pass
