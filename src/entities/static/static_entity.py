from ..entity import Entity


class StaticEntity(Entity):
    # по умолчанию статические объекты нельзя будет удалять
    def is_dead(self) -> bool:
        return False
