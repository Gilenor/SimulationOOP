from .creature import Creature

from src.worlds import World
from src.entities.static import Grass
from src.entities.entity import Entity


class Herbivore(Creature):
    _targets = (Grass,)

    def __init__(self, health: int, speed: int):
        super().__init__(health, speed)

    def interact_with_target(self, target: Entity, world: World):
        if not isinstance(target, self._targets):
            print(f"Error: {target} id not valid type target for Herbivore")
            return

        target.hit()
