import random

from typing import List, Type, Optional, Tuple

from src.worlds import World
from src.position import Position
from src.entities.entity import Entity


Path = List[Position]
PathCeil = Position
Target = Optional[Entity]


class PathFinder():
    def __init__(self, targets: List[Type]) -> None:
        self._targets = targets

    # простая реализация поиска в ширину
    # возвращается путь к первой найденной ближайшей цели
    def get_path_to_target(self, start: Position, world: World) -> Tuple[Path, Target]:
        queue: Path = [start]
        visited = {start: start}
        vertex: Position
        entity: Target = None

        neighbors = [
            (0, 1),   # Up
            (1, 0),   # Right
            (0, -1),  # Down
            (-1, 0),  # Left
        ]

        # WARNING: если стартовой позиции нет на карте, то путь не ищется
        #          в будущем возможны ошибки, если измениться работа с картой
        if not world.is_exist(start):
            return [], None

        while queue:
            vertex = queue.pop(0)  # left/first
            entity = world.get_entity_at(vertex)

            # найдена ближайшая цель
            if type(entity) in self._targets:
                break

            # перемешиваем для разнообразия получаемых путей
            random.shuffle(neighbors)

            for neighbor in neighbors:
                new_vertex = vertex + neighbor

                # если позиции не существует для карты или она уже проверена
                if not world.is_exist(new_vertex) or new_vertex in visited:
                    continue

                # ключ - куда пришел, значение - откуда
                visited[new_vertex] = vertex
                queue.append(new_vertex)
        else:
            return [], entity

        # вычисляем путь до цели
        path: Path = []

        while vertex != start:
            path.insert(0, vertex)
            vertex = visited[vertex]

        # ToDo: подумать, нужно ли в путь записывать стартовую позицию
        return path, entity
