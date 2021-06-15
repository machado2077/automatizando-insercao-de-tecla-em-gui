from time import sleep

class PynputKeyboardController:
    def __init__(self, controller) -> None:
        self.__controller = controller

    def start_key_press(self, key):
        self.__controller.tap(key)
        sleep(0.8)