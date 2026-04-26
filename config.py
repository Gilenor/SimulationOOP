import os

from types import SimpleNamespace
from typing import Dict, Type, List

from src.entities import Entity, Grass, Herbivore, Predator, Rock, Tree
from src.worlds.world_2d import World2D
from src.position import Position


_main_dir = os.path.split(os.path.abspath(__file__))[0]
DATA_DIR = os.path.join(_main_dir, "data")
IMAGES_DIR = os.path.join(DATA_DIR, "images")


# размеры мира
WORLD_WIDTH = 10
WORLD_HEIGHT = 10
WORLD_SIZE = (WORLD_WIDTH, WORLD_HEIGHT)

WINDOW_SIZE = (500, 500)

GRID_COLOR = (126, 126, 126)
BACKGROUND_COLOR = (0, 0, 0)

CONSOLE_TEXT_SPRITES: Dict[Type[Entity], str] = {
    Tree: "T",
    Rock: "R",
    Grass: "G",
    Predator: "P",
    Herbivore: "H",
}

PYGAME_SPRITES: Dict[Type[Entity], str] = {
    Tree: os.path.join(IMAGES_DIR, "tree.png"),
    Rock: os.path.join(IMAGES_DIR, "stone.png"),
    Grass: os.path.join(IMAGES_DIR, "grass.png"),
    Predator: os.path.join(IMAGES_DIR, "wolf.png"),
    Herbivore: os.path.join(IMAGES_DIR, "cow.png"),
}

PREDATOR = SimpleNamespace(speed=1, health=15, attack=5)

HERBIVORE = SimpleNamespace(speed=1, health=10)

_NEIGHBORS = {}


# предпосчет соседей для всех клеток для оптимизации поиска
def _fill_neighbors():
    world = World2D(WORLD_WIDTH, WORLD_HEIGHT)

    for x in range(WORLD_WIDTH):
        for y in range(WORLD_HEIGHT):
            pos = Position(x, y)

            _NEIGHBORS[pos] = list(filter(world.is_valid, _neighbors(pos)))
    print("Neighbors len:", len(_NEIGHBORS))


def _neighbors(cell: Position):
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    return [cell + n for n in neighbors]


def get_neighbors(cell: Position) -> List[Position]:
    return _NEIGHBORS.get(cell, [])


_fill_neighbors()
