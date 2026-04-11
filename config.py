from types import SimpleNamespace

# размеры мира
WORLD_WIDTH = 5
WORLD_HEIGHT = 5

CONSOLE_TEXT_SPRITES = {
    "Empty": '-',
    "Tree": 'T',
    "Rock": 'R',
    "Grass": 'G',
    "Predator": 'P',
    "Herbivore": 'H',
}

PREDATOR = SimpleNamespace(
    speed=2,
    health=15,
    attack=3
)

HERBIVORE = SimpleNamespace(
    speed=1,
    health=10
)
