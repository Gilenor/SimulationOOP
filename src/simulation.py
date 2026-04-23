import time
from typing import List

from src.actions import MoveEntitiesAction, SpawnEntitiesAction, RespawnEntitiesAction, RemoveDeadEntitiesAction
from src.actions.factories import (
    GrassFactory,
    HerbivoreFactory,
    PredatorFactory,
    RockFactory,
    TreeFactory,
)


from src.actions import Action
from src.renders import Render
from src.worlds import World


class Simulation:
    def __init__(self, world: World, render: Render):
        self._world = world
        self._render = render
        self._move_counter = 0
        self._init_actions: List[Action] = [
            # SpawnEntitiesAction(RockFactory, count=5),
            # SpawnEntitiesAction(TreeFactory, count=5),
            # SpawnEntitiesAction(GrassFactory(), count=3),
            SpawnEntitiesAction(PredatorFactory(), count=2),
            SpawnEntitiesAction(HerbivoreFactory(), count=2)
        ]
        self._turn_actions = [
            MoveEntitiesAction(),
            RemoveDeadEntitiesAction(),
            RespawnEntitiesAction(GrassFactory(), min_count=5, spawn_count=1),
            RespawnEntitiesAction(PredatorFactory(), min_count=4, spawn_count=1),
            RespawnEntitiesAction(HerbivoreFactory(), min_count=8, spawn_count=1),
        ]

    def next_turn(self):
        self._render.clear()

        for action in self._turn_actions:
            action.execute(self._world)

        self._move_counter += 1
        self._render.render(self._world)

    def start_simulation(self):
        self._initialize()

        while self._move_counter < 40:
            self.next_turn()
            time.sleep(1)

    def pause_simulation(self):
        pass

    # ---------- private ------------------------------------------------------

    def _initialize(self):
        for action in self._init_actions:
            action.execute(self._world)
