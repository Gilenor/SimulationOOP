from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds import World


class Render(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def render(self, world: 'World'):
        pass
