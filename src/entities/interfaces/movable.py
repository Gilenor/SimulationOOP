from abc import ABC, abstractmethod

from src.utils.path_finder import Path
from src.worlds import World


class Movable(ABC):
    @abstractmethod
    def make_move(self, world: World):
        pass

    @abstractmethod
    def move(self, path: Path, world: World):
        pass
