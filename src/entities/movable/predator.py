from .creature import Creature

from src.worlds import World
from src.entities.entity import Entity
from src.entities.movable import Herbivore
from src.utils.path_finder import PathFinder


class Predator(Creature):
    _targets = (Herbivore,)

    def __init__(self, health: int, speed: int, attack: int):
        super().__init__(health, speed)
        self._attack = attack

    def make_move(self, world: World):
        super().make_move(world)

    def interact_with_target(self, target: Entity, world: World):
        if not isinstance(target, self._targets):
            print(f"Error: {target} id not valid type target for Predator")
            return

        target.hit(self._attack)
