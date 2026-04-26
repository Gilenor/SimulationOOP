from .sprite import Sprite


class PygameSprite(Sprite):
    def __init__(self, data):
        self._data = data

    def __str__(self) -> str:
        # ToDo: подумать над возможными ошибками при возвращении data
        return self._data

    @property
    def data(self):
        return self._data
