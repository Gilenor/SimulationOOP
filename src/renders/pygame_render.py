import pygame as pg

import config as conf

from typing import Tuple

from .render import Render
from .sprites.pygame_sprite_map import PygameSpriteMap

from src.worlds import World


class PygameRender(Render):
    def __init__(self, sprite_map: PygameSpriteMap):
        super().__init__()

        self._sprite_map = sprite_map

        # Initialise screen
        pg.init()
        pg.display.set_caption('Simulation')

        self._screen = pg.display.set_mode(conf.WINDOW_SIZE, pg.RESIZABLE)
        self._aspect_ratio = 1

        # Fill background
        background = pg.Surface(self._screen.get_size())
        self._background = background.convert()
        self._background_pos = (0, 0)
        self.resize()

    def render(self, world: World):
        self._draw_grid()
        self._draw_entities(world)
        self._screen.blit(self._background, self._background_pos)
        pg.display.flip()

    def clear(self):
        # self._background.fill((0, 0, 0))
        self._screen.fill(conf.BACKGROUND_COLOR)

    def resize(self):
        screen_width, screen_height = self._screen.get_size()

        # сохраняем квадратные пропорции
        aspect_ratio_width = screen_width / conf.WORLD_WIDTH
        aspect_ratio_height = screen_height / conf.WORLD_HEIGHT
        self._aspect_ratio = min(aspect_ratio_width, aspect_ratio_height)

        view_size = self._mult_by_scalar(conf.WORLD_SIZE, self._aspect_ratio)

        print("Background changed from:", self._background.get_size(), end="")
        self._background = pg.transform.scale(self._background, view_size)
        print(", to:", self._background.get_size(), "\n")

        self._background_pos = (
            (screen_width - view_size[0]) / 2,
            (screen_height - view_size[1]) / 2,
        )

        # пересчитывает размеры спрайтов
        self._sprite_map.rescale(self._get_cell_size())

    # ========== private methods ==============================================

    def _mult_by_scalar(self, nums, scalar):
        return tuple(num * scalar for num in nums)

    def _add_scalar(self, nums, scalar):
        return tuple(num + scalar for num in nums)

    def _draw_grid(self):
        cell_width, cell_height = self._get_cell_size()

        surface = self._background
        surface.fill(conf.BACKGROUND_COLOR)

        view_size = surface.get_size()

        # рисуем горизонтали
        for row in range(conf.WORLD_HEIGHT + 1):
            y = min(row * cell_height, view_size[1] - (cell_height / 100))
            x = view_size[0]
            pg.draw.line(surface, conf.GRID_COLOR, (0, y), (x, y))

        # рисуем вертикали
        for col in range(conf.WORLD_WIDTH + 1):
            y = view_size[1]
            x = min(col * cell_width, view_size[0] - (cell_width / 100))
            pg.draw.line(surface, conf.GRID_COLOR, (x, 0), (x, y))

    def _draw_entities(self, world: World):
        entities = world.get_entities()
        cell_width, cell_height = self._get_cell_size()

        for entity in entities:
            position = world.get_entity_position(entity)
            sprite = self._sprite_map.get_sprite(entity)

            #image = self._load_image(
            #    sprite.data, (cell_width, cell_height), -1)
            image = sprite.data

            image_pos = (
                position.x * cell_width,
                position.y * cell_height
            )
            self._background.blit(image, image_pos)

    def _get_cell_size(self) -> Tuple:
        return (
            self._background.get_size()[0] / conf.WORLD_WIDTH,
            self._background.get_size()[1] / conf.WORLD_HEIGHT
        )

    def _load_image(self, path, cell, colorkey=None):
        image = pg.image.load(path)

        size = image.get_size()
        scale = min(cell[0] / size[0], cell[1] / size[1])

        size = (size[0] * scale, size[1] * scale)
        image = pg.transform.scale(image, size)

        image = image.convert()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pg.RLEACCEL)

        return image
