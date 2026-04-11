from typing import Tuple


class Position(object):
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return f"x: {self._x}, y: {self._y}"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Position):
            return self.get_coords() == value.get_coords()
        if isinstance(value, Tuple):
            return self.get_coords() == value

        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.get_coords())

    def get_coords(self) -> Tuple:
        return (self._x, self._y)

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y
