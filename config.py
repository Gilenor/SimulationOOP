from types import SimpleNamespace
from src.entities import Tree, Rock, Grass, Predator, Herbivore
from src.utils.path_finder import PathCeil


# размеры мира
WORLD_WIDTH = 30
WORLD_HEIGHT = 20

CONSOLE_TEXT_SPRITES = {
    PathCeil: "*",  # добавил для теста, проверить выводимый путь
    Tree: "T",
    Rock: "R",
    Grass: "G",
    Predator: "P",
    Herbivore: "H",
}

PREDATOR = SimpleNamespace(speed=1, health=15, attack=5)

HERBIVORE = SimpleNamespace(speed=1, health=10)
