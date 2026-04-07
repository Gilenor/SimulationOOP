from typing import Tuple


class Position(object):
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return f"x: {self._x}, y: {self._y}"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Position):
            return NotImplemented
        return self.get_coords() == value.get_coords()

    def __hash__(self) -> int:
        return hash(self.get_coords())

    def get_coords(self) -> Tuple:
        return (self._x, self._y)


pos1 = Position(1, 1)
pos2 = Position(1, 1)

print(pos1 == pos2)
