from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def __init__(self):
        pass
