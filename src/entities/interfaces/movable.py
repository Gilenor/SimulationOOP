from abc import abstractmethod, ABC
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.worlds import World
    from src.utils.path_finder import Path


class Movable(ABC):
    @abstractmethod
    def make_move(self, world: "World"):
        pass

    @abstractmethod
    def move(self, path: "Path", world: "World"):
        pass
