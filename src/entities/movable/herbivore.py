from src.entities.entity import Entity
from src.entities.static import Grass
from src.worlds import World

from .creature import Creature


class Herbivore(Creature):
    _targets = (Grass,)

    def __init__(self, health: int, speed: int):
        super().__init__(health, speed)

    def interact_with_target(self, target: Entity, world: World):
        if not isinstance(target, self._targets):
            print(f"Error: {target} id not valid type target for Herbivore")
            return

        # WARNING: нужно подумать о систему урона для травы и о том
        #          как определять насколько поглощение травы будет
        #          восстанавливать здоровье или жизнь Herbivore
        target.take_damage(1)
