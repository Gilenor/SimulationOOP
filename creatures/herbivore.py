from .creature import Creature


class Herbivore(Creature):
    def __init__(self, health: int, speed: int):
        super().__init__(health, speed)

    def make_move(self):
        return super().make_move()
