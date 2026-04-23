from src.worlds import World

from .action import Action


class RemoveDeadEntitiesAction(Action):
    def execute(self, world: World):
        entities = world.get_entities()

        for entity in entities:
            if entity.is_dead():
                world.remove_entity(entity)
