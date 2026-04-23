from ..entity import Entity


class StaticEntity(Entity):
    def is_dead(self) -> bool:
        return False
