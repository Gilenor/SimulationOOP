from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def is_dead(self) -> bool:
        pass

    # def __del__(self):
    #    print(f"{self} id: {id(self)} was deleted")

    def __str__(self) -> str:
        return type(self).__name__
