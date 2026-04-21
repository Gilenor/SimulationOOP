from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List, Tuple, Type, Optional

if TYPE_CHECKING:
    from src.entities.entity import Entity
    from src.position import Position


class World(ABC):
    @abstractmethod
    def add_entity(self, entity: "Entity", position: "Position"):
        pass

    @abstractmethod
    def remove_entity(self, entity: "Entity"):
        pass

    @abstractmethod
    def move_entity_to(self, entity: "Entity", new_pos: "Position"):
        pass

    @abstractmethod
    def get_entities(self, entity_type: Optional[Type] = None) -> List["Entity"]:
        pass

    @abstractmethod
    def get_entity_position(self, entity: "Entity") -> Optional["Position"]:
        pass

    @abstractmethod
    def get_entity_at(self, position: "Position") -> Optional["Entity"]:
        pass

    @abstractmethod
    def get_empty_positions(self) -> List["Position"]:
        pass

    @abstractmethod
    def get_dimensions(self) -> Tuple:
        pass

    @abstractmethod
    def is_free(self, position: "Position") -> bool:
        pass

    @abstractmethod
    def is_exist(self, position: "Position") -> bool:
        pass
