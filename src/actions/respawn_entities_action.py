import random

from .action import Action
from .factories import EntityFactory

from src.worlds import World


class RespawnEntitiesAction(Action):
    def __init__(self, entity_factory: EntityFactory, min_count: int, spawn_count: int):
        # factory for specific Entity type
        self._entity_factory = entity_factory
        self._entity_type = entity_factory.entity_type
        self._min_count = min_count
        self._spawn_count = spawn_count

    def execute(self, world: World):
        entities_count = len(world.get_entities(self._entity_type))
        free_positions = world.get_empty_positions()
        spawn_count = int(entities_count < self._min_count) * self._spawn_count

        for i in range(spawn_count):
            # WARNING: нужно ли выбрасывать исключение?
            if not free_positions:
                return

            pos = random.choice(free_positions)
            entity = self._entity_factory()
            # WARNING: потенциальная ошибка, если клетка окажется занятой
            world.add_entity(entity, pos)
            free_positions.remove(pos)
