from worlds import World2D
from renders import ConsoleRender
from simulation import Simulation

from position import Position
from sprites import ConsoleTextSpriteMap
from entities import Tree, Rock, Grass

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
world.add_entity(Grass(), Position(0,0))
print(world.get_empty_positions())
print(hash((0,0)) in world._entities)
print(Position(0,0) in world._entities)


positions = {}
pos = Position(0, 0)
positions[pos] = str(hash(pos))
positions[(0,0)] = str(hash(pos))

positions = set()
positions.add(Position(0, 0))
positions.add((0, 0))

print(positions)


print("        (0, 0):", hash((0, 0)))
print("        (0, 0):", hash((0, 0)))
print()

print("Position(0, 0):", hash(Position(0, 0)))
print("Position(0, 0):", hash(Position(0, 0)))
print()

print("        (0, 0) in positions:", (0, 0) in positions)
print("Position(0, 0) in positions:", Position(0, 0) in positions)
print()


#simulation.next_turn()
#simulation.start_simulation()
