from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self) -> str:
        return type(self).__name__
