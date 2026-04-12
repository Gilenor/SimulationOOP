from .creature import Creature

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds import World


class Predator(Creature):
    def __init__(self, health: int, speed: int, attack: int):
        super().__init__(health, speed)

    def make_move(self, world: 'World'):
        print("Predator: ", world.get_entity_position(self))
        return super().make_move(world)
