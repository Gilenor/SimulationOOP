from types import SimpleNamespace
from typing import Dict, Type

from src.entities import Entity, Grass, Herbivore, Predator, Rock, Tree

# размеры мира
WORLD_WIDTH = 30
WORLD_HEIGHT = 20

CONSOLE_TEXT_SPRITES: Dict[Type[Entity], str] = {
    Tree: "T",
    Rock: "R",
    Grass: "G",
    Predator: "P",
    Herbivore: "H",
}

PREDATOR = SimpleNamespace(speed=1, health=15, attack=5)

HERBIVORE = SimpleNamespace(speed=1, health=10)
