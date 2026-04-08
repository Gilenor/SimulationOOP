import time
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from actions import Action
    from worlds import World
    from renders import Render


class Simulation():
    def __init__(self, world: 'World', render: 'Render'):
        self._world = world
        self._render = render
        self._actions = List['Action']
        self._move_counter = 0

    def next_turn(self):
        self._move_counter += 1
        self._render.render(self._world)

    def start_simulation(self):
        while True:
            self.next_turn()
            time.sleep(1)

    def pause_simulation(self):
        pass
