from random import uniform
from time import sleep
from pynput.keyboard import Controller

class PynputKeyboardController:
    def __init__(self) -> None:
        self.__controller = Controller()

    def __randomize_sleep_time(self):
        inferior_limit = 0.7
        upper_limit = 0.9
        real_num = uniform(inferior_limit, upper_limit)
        return float(f'{real_num:.3}')

    def start_key_press(self) -> None:
        self.__controller.type('typing... ')
        time = self.__randomize_sleep_time()
        sleep(time) #O sleep precisa estar depois do .tap(key)


def plug_app(app) -> None:
    response_adapter = PynputKeyboardController()
    app.response_port.response_adapter = response_adapter