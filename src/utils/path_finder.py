# import random

# from functools import lru_cache, cache
from typing import List, Tuple, Type

from src.entities.entity import Entity
from src.position import Position
from src.worlds.world import World

import config as conf

Path = List[Position]
PathCeil = Position


class PathFinder:
    def __init__(self, targets: Tuple[Type[Entity], ...]) -> None:
        self._targets = targets

    # простая реализация поиска в ширину
    # возвращается путь к первой найденной ближайшей цели
    def get_path_to_target(self, start: Position, world: World) -> Path:
        queue: Path = [start]
        visited = {start: start}
        vertex: Position

        # neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down  # Right  # Up  # Left

        # WARNING: если стартовой позиции нет на карте, то путь не ищется
        #          в будущем возможны ошибки, если измениться работа с картой
        if not world.is_valid(start):
            return []

        while queue:
            vertex = queue.pop(0)  # left/first

            # чтобы не писать перехват исключений проще сразу проверить
            # стоит ли кто-то на текущей клетке
            if not world.is_free(vertex):
                entity = world.get_entity_at(vertex)

                # найдена ближайшая цель
                if type(entity) in self._targets:
                    break

                # если координата занята кем-то кроме нашей цели, "обходим" ее
                if vertex != start:
                    continue

            # перемешиваем для разнообразия получаемых путей
            neighbors = _get_neighbors(vertex)
            # random.shuffle(neighbors)

            for neighbor in neighbors:
                new_vertex = neighbor  # vertex + neighbor

                # пропускаем если позиция: не валидная или уже проверена
                # if (not world.is_valid(new_vertex)) or new_vertex in visited:
                if new_vertex in visited:
                    continue

                # ключ - куда пришел, значение - откуда
                visited[new_vertex] = vertex
                queue.append(new_vertex)
        else:
            return []

        # вычисляем путь до цели
        path: Path = []

        while vertex != start:
            path.insert(0, vertex)
            vertex = visited[vertex]

        # ToDo: подумать, нужно ли в путь записывать стартовую позицию
        return path

#@lru_cache
#@cache
def _get_neighbors(cell: Position) -> List[Position]:
    # neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # return [cell + n for n in neighbors]
    # if cell in conf.NEIGHBORS:
    return conf.get_neighbors(cell)
    # print("[WARNING]: У клетки нет соседей!!!")
