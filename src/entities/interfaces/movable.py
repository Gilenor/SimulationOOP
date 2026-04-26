from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.utils.path_finder import Path
    from src.worlds.world import World


class Movable(ABC):
    @abstractmethod
    def make_move(self, world: "World"):
        pass

    @abstractmethod
    def move(self, path: "Path", world: "World"):
        pass
