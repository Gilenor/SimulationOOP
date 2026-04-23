from typing import List

from src.entities.movable import MovableEntity
from src.worlds import World

from .action import Action


class MoveEntitiesAction(Action):
    def execute(self, world: World):
        entities: List[MovableEntity] = world.get_entities(entity_type=MovableEntity)

        for entity in entities:
            if not entity.is_dead():
                entity.make_move(world)
