from typing import List

from .action import Action

from src.worlds import World
from src.entities.entity import Entity
from src.entities.interfaces import Movable


class MoveEntitiesAction(Action):
    def execute(self, world: World):
        entities = world.get_entities(entity_type=Movable)

        for entity in entities:
            if not entity.is_dead():
                entity.make_move(world)
