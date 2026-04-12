from .creature import Creature

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds import World


class Herbivore(Creature):
    def __init__(self, health: int, speed: int):
        super().__init__(health, speed)

    def make_move(self, world: 'World'):
        print("Herbivore: ", world.get_entity_position(self))
        return super().make_move(world)
