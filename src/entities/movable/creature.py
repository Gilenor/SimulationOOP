from abc import abstractmethod
from typing import Tuple, Type

from src.entities.destroyable_entity import DestroyableEntity
from src.entities.entity import Entity
from src.utils.path_finder import Path, PathFinder
from src.worlds import World

from .movable_entity import MovableEntity


class Creature(DestroyableEntity, MovableEntity):
    _targets: Tuple[Type[Entity]]

    @abstractmethod
    def __init__(self, health: int, speed: int):
        DestroyableEntity.__init__(self, health)

        self._speed = speed
        self._path_finder = PathFinder(self._targets)

    def make_move(self, world: World):
        try:
            position = world.get_entity_position(self)
            path = self._path_finder.get_path_to_target(position, world)

            # print(f"{str(self):<10}: {position}, target: {str(target):<10}, path to target: {path}")

            if len(path) == 1:
                target = world.get_entity_at(path[-1])
                # взаимодействуем с целью
                self.interact_with_target(target, world)
            else:
                # идем к цели
                self.move(path, world)

        except Exception as e:
            print(e)

    def move(self, path: Path, world: World):
        if not path:
            return

        # WARNING: если в полученном пути до цели какая-то клетка будет занята
        #          то возможна ошибка консистентности карты, для чего
        #          на всякий случай делаются проверки на доступность хода
        #          возможно лучше ГАРАНТИРОВАННО получать только "чистый" путь
        max_step = min(len(path) - 1, self._speed)
        for step in range(max_step, -1, -1):
            if world.is_free(path[step]):
                world.move_entity_to(self, path[step])

    # переопределить в дочернем классе, для взамодействия с целью
    def interact_with_target(self, target: Entity, world: World):
        """часть шаблонного метода make_move отвечающая за взаимодействие с целью"""
        pass
