from ..entity import Entity
# from .static_entity import StaticEntity

# надо подумать как лучше определить иерархию наследования
# Grass должна быть статичной, но вместе с тем же разрушаемой


class Grass(Entity):
    def __init__(self, health: int = 1):
        super().__init__(health)

    def hit(self, damage: int = 1):
        return super().hit(damage)
