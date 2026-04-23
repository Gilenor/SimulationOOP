from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.worlds import World


class Action(ABC):
    @abstractmethod
    def execute(self, world: "World"):
        pass
