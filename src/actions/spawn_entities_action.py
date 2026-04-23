import random

from .action import Action
from .factories import EntityFactory

from src.worlds import World


class SpawnEntitiesAction(Action):
    def __init__(self, entity_factory: EntityFactory, count: int):
        # factory for specific Entity type
        self._entity_factory = entity_factory
        self._count = count

    def execute(self, world: World):
        free_positions = world.get_empty_positions()

        for i in range(self._count):
            # WARNING: нужно ли выбрасывать исключение?
            if not free_positions:
                return

            pos = random.choice(free_positions)
            entity = self._entity_factory()
            # WARNING: потенциальная ошибка, если клетка окажется занятой
            world.add_entity(entity, pos)
            free_positions.remove(pos)
