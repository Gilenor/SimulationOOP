from typing import Tuple, NamedTuple


class Position(NamedTuple):
    x: int
    y: int

    # def __del__(self):
    #    print(f"{self} id: {id(self)} was deleted")

    def __str__(self) -> str:
        return f"(x: {self.x}, y: {self.y})"

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, value: object) -> "Position":
        if isinstance(value, Position):
            return Position(self.x + value.x, self.y + value.y)
        if isinstance(value, Tuple):
            return Position(self.x + value[0], self.y + value[1])

        return NotImplemented

    def get_coords(self) -> Tuple[int, int]:
        return self
