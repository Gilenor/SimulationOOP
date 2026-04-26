from abc import ABC, abstractmethod, abstractproperty


class Sprite(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractproperty
    def data(self):
        pass
