import time
import config

from actions import SpawnEntitiesAction
from actions.factories import GrassFactory, TreeFactory
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from actions import Action
    from worlds import World
    from renders import Render


class Simulation():
    def __init__(self, world: 'World', render: 'Render'):
        self._world = world
        self._render = render
        self._move_counter = 0
        self._init_actions: List['Action'] = [
            SpawnEntitiesAction(TreeFactory, count=10),
            SpawnEntitiesAction(GrassFactory, count=10),
        ]
        self._turn_actions = []

    def next_turn(self):
        self._move_counter += 1
        self._render.render(self._world)

    def start_simulation(self):
        self._initialize()
        self.next_turn()

        #while True:
        #    self.next_turn()
        #    time.sleep(1)

    def pause_simulation(self):
        pass

    # ---------- private ------------------------------------------------------

    def _initialize(self):
        for action in self._init_actions:
            action.execute(self._world)
