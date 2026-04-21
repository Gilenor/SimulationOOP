from abc import abstractmethod
from typing import List, Type

from src.worlds import World
from src.position import Position
from src.entities.entity import Entity
from src.entities.interfaces import Movable
from src.utils.path_finder import PathFinder, Path, Target


class Creature(Entity, Movable):
    _targets: List[Type]

    @abstractmethod
    def __init__(self, health: int, speed: int):
        self.health = health
        self.speed = speed
        self.path_finder = PathFinder(self._targets)

    @property
    def path_finder(self) -> PathFinder:
        return self._path_finder

    @path_finder.setter
    def path_finder(self, pf: PathFinder):
        self._path_finder = pf

    def make_move(self, world: World):
        position = world.get_entity_position(self)
        path, target = self.path_finder.get_path_to_target(position, world)
        # print(f"{str(self):<10}: {position}, target: {str(target):<10}, path to target: {path}")

        if len(path) == 1:
            # взаимодействуем с целью
            self.interact_with_target(target, world)
        else:
            # идем к цели
            self.move(path, world)

    def move(self, path: Path, world: World):
        if not Path:    return

        if world.is_free(path[0]):
            world.move_entity_to(self, path[0])

    # переопределить в дочернем классе, для взамодействия с целью
    def interact_with_target(self, target: Target, world: World):
        pass
