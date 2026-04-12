from abc import ABC, abstractmethod


class Sprite(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class ConsoleSprite(Sprite):
    def __init__(self, data):
        self._data = data

    def __str__(self) -> str:
        return super().__str__()


class ConsoleTextSprite(Sprite):
    def __init__(self, data):
        self._data = data

    def __str__(self) -> str:
        # ToDo: подумать над возможными ошибками при возвращении data
        return self._data
