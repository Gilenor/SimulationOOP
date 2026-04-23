from blinker import signal

destroyed_signal = signal('object-destroyed')


class Destroyable():
    def __init__(self):
        self._exist = True
        print(f"{self} now is existing")

    def destroy(self):
        if not self._exist:
            return

        # Отправляем сигнал в «эфир»
        destroyed_signal.send(self)
        self._exist = False
        print(f"{self} id: {id(self)}, was destroyed")

    def is_exist(self) -> bool:
        return self._exist
