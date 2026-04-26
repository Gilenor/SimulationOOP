import pygame as pg

from typing import Dict, Type, Tuple

from .sprite import Sprite
from .pygame_sprite import PygameSprite
from .sprite_map import SpriteMap

from src.entities.entity import Entity

from config import PYGAME_SPRITES


class PygameSpriteMap(SpriteMap):
    def __init__(self):
        self._sprite_map: Dict[Type[Entity], pg.Image] = {
            sprite_type: self._load_image(sprite_path, -1)
            for sprite_type, sprite_path in PYGAME_SPRITES.items()
        }
        #self._sprite_map = PYGAME_SPRITES

    def get_sprite(self, entity: Entity) -> Sprite:
        # WARNING: возможно получать спрайт по типу класса не лучшая идея
        data = self._sprite_map.get(type(entity))

        return PygameSprite(data)

    def rescale(self, cell_size: Tuple):
        for sprite_type, image in self._sprite_map.items():
            size = image.get_size()
            scale = min(cell_size[0] / size[0], cell_size[1] / size[1])

            size = (size[0] * scale, size[1] * scale)
            scaled_image = pg.transform.scale(image, size)
            self._sprite_map[sprite_type] = scaled_image.convert()

    # ========== private methods ==============================================

    def _load_image(self, path, colorkey=None):
        image = pg.image.load(path)

        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pg.RLEACCEL)

        return image
