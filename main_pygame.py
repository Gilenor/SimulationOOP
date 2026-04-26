import pygame as pg
import config as conf

from src.renders.pygame_render import PygameRender
from src.renders.sprites.pygame_sprite_map import PygameSpriteMap
from src.worlds import World, World2D
from src.simulation import Simulation
from src.entities import Rock, Grass, Herbivore
from src.position import Position


def main():
    timer = pg.time.Clock()
    render = PygameRender(PygameSpriteMap())
    world = World2D(conf.WORLD_WIDTH, conf.WORLD_HEIGHT)
    # world.add_entity(Grass(), Position(0, 0))
    # world.add_entity(Rock(), Position(1, 0))
    # world.add_entity(Rock(), Position(1, 1))
    # world.add_entity(Rock(), Position(0, 1))
    # world.add_entity(Herbivore(1, 1), Position(4, 4))
    simulation = Simulation(world, render)

    simulation.start_simulation()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.VIDEORESIZE:
                render.resize()
                print("new size:", event.dict["size"])

        # render.clear()
        # render.render(world)
        simulation.next_turn()
        print("FPS:", timer.get_fps())

        timer.tick(600)


if __name__ == "__main__":
    #import cProfile
    #import pstats

    #cProfile.run("main()", "profile.stats")
    #stats = pstats.Stats("profile.stats")
    #stats.sort_stats("cumulative").print_stats(20)
    main()
