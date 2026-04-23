from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List, Tuple, Type, Optional

#from src.entities.interfaces.destroyable import destroyed_signal

if TYPE_CHECKING:
    from src.entities.entity import Entity
    from src.position import Position


class World(ABC):
    # def __init__(self) -> None:
        # Подписываемся на глобальный сигнал уничтожения entity
    #    print("Init World")
    #    destroyed_signal.connect(self.remove_entity)

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
    def get_entity_position(self, entity: "Entity") -> "Position":
        pass

    @abstractmethod
    def get_entity_at(self, position: "Position") -> "Entity":
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
    def is_valid(self, position: "Position") -> bool:
        pass

    @abstractmethod
    def is_exist(self, entity: "Entity") -> bool:
        pass
