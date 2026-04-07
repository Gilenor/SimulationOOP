from worlds import World2D
from renders import ConsoleRender
from simulation import Simulation
from sprites import ConsoleTextSpriteMap
from entities import Tree, Rock, Grass, Entity

from config import WORLD_WIDTH, WORLD_HEIGHT


simulation = Simulation(
    world=World2D(WORLD_WIDTH, WORLD_HEIGHT),
    render=ConsoleRender(ConsoleTextSpriteMap()),
)

simulation.next_turn()


print(type(Rock))
print(issubclass(Rock, Entity))
print(Rock.__name__)
input(">>> Type ENTER for exit...")
