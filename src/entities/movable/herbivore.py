from .creature import Creature

from src.worlds import World
from src.entities.static import Grass
from src.utils.path_finder import PathFinder


class Herbivore(Creature):
    _targets = [Grass]

    def __init__(self, health: int, speed: int):
        super().__init__(health, speed)

    def make_move(self, world: World):
        super().make_move(world)
