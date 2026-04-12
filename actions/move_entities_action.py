from .action import Action
from entities import Movable

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from worlds import World


class MoveEntitiesAction(Action):
    def execute(self, world: 'World'):
        entities: List[Movable] = world.get_entities(entity_type=Movable)

        for entity in entities:
            entity.make_move(world)
