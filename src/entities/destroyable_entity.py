from .entity import Entity
from .interfaces.destroyable import Destroyable


class DestroyableEntity(Entity, Destroyable):
    def __init__(self, health: int):
        Destroyable.__init__(self, health)

    def is_dead(self) -> bool:
        return Destroyable.is_dead(self)
