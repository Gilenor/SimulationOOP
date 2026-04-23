from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def __init__(self, health: int) -> None:
        self._health = health

    #def __del__(self):
    #    print(f"{self} id: {id(self)} was deleted")

    def __str__(self) -> str:
        return type(self).__name__

    def hit(self, damage: int = 0):
        self._health -= damage

    def is_dead(self) -> bool:
        return self._health <= 0
