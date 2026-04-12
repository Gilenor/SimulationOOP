import random

from .action import Action
from .factories import EntityFactory

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds import World


class SpawnEntitiesAction(Action):
    def __init__(self, entity_factory: EntityFactory, count: int):
        # factory for specific Entity type
        self.entity_factory = entity_factory
        self.count = count

    def execute(self, world: 'World'):
        for i in range(self.count):
            free_positions = world.get_empty_positions()

            # нужно ли выбрасывать исключение?
            if not free_positions:
                return

            pos = random.choice(free_positions)
            entity = self.entity_factory()
            world.add_entity(entity, pos)
