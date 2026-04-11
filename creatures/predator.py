from .creature import Creature


class Predator(Creature):
    def __init__(self, health: int, speed: int, attack: int):
        super().__init__(health, speed)

    def make_move(self):
        return super().make_move()
