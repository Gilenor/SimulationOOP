from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds import World


class Action(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def execute(self, game_map: 'World'):
        pass
