from config import WORLD_HEIGHT, WORLD_WIDTH
from src.entities import Entity, Grass, Rock, Tree
from src.position import Position
from src.renders import ConsoleRender
from src.renders.sprites import ConsoleTextSpriteMap
from src.simulation import Simulation
from src.worlds import World2D

world = World2D(WORLD_WIDTH, WORLD_HEIGHT)

simulation = Simulation(world=world, render=ConsoleRender(ConsoleTextSpriteMap()))


# simulation.next_turn()
simulation.start_simulation()
