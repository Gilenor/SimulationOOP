from ..entity import Entity
from abc import abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds import World


class Movable(Entity):
    @abstractmethod
    def make_move(self, world: 'World'):
        pass
