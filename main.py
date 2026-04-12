from worlds import World2D
from renders import ConsoleRender
from simulation import Simulation

from position import Position
from entities import Tree, Rock, Grass
from renders.sprites import ConsoleTextSpriteMap

from config import WORLD_WIDTH, WORLD_HEIGHT

world = World2D(WORLD_WIDTH, WORLD_HEIGHT)
#world.add_entity(Grass(), Position(2, 2))
#world.add_entity(Rock(), Position(3, 6))
#world.add_entity(Tree(), Position(5, 8))
#world.add_entity(Rock(), Position(2, 8))

simulation = Simulation(
    world=world,
    render=ConsoleRender(ConsoleTextSpriteMap()),
)

#simulation.next_turn()
simulation.start_simulation()