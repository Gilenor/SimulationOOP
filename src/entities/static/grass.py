from ..destroyable_entity import DestroyableEntity
from .static_entity import StaticEntity

# надо подумать как лучше определить иерархию наследования
# Grass должна быть статичной, но вместе с тем же разрушаемой


class Grass(StaticEntity, DestroyableEntity):
    def __init__(self, health: int = 1):
        StaticEntity.__init__(self)
        DestroyableEntity.__init__(self, health)

    def is_dead(self) -> bool:
        return DestroyableEntity.is_dead(self)
