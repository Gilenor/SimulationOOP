# from blinker import signal

# destroyed_signal = signal('object-destroyed')


class Destroyable:
    def __init__(self, health: int):
        self._health = health
        # print(f"{self} now is existing")

    """ def destroy(self):
        if self.is_dead():
            return

        # Отправляем сигнал в «эфир»
        destroyed_signal.send(self)
        print(f"{self} id: {id(self)}, was destroyed") """

    def take_damage(self, damage: int):
        self._health -= damage

    def is_dead(self) -> bool:
        return self._health <= 0
