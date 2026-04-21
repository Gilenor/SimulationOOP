from .creature import Creature

from src.worlds import World
from src.entities.movable import Herbivore
from src.utils.path_finder import PathFinder


class Predator(Creature):
    _targets = [Herbivore]

    def __init__(self, health: int, speed: int, attack: int):
        super().__init__(health, speed)
        self.attack = attack

    def make_move(self, world: World):
        super().make_move(world)
