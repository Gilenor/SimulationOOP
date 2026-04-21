from typing import List

from .action import Action

from src.worlds import World
from src.entities.interfaces import Movable


class MoveEntitiesAction(Action):
    def execute(self, world: World):
        entities: List[Movable] = world.get_entities(entity_type=Movable)

        for entity in entities:
            entity.make_move(world)
