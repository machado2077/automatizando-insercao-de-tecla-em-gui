from time import sleep
from random import uniform
from pynput.keyboard import Controller
from .keyboard_event_mapper import keyboard_event_mapper as key_event
from .abstract_classes.abstract_keyboard_event_response import AbstractKeyboardEventResponse

keyboard_controller = Controller()


class PynputKeyboardEventResponse(AbstractKeyboardEventResponse):
    def __init__(self) -> None:
        super().__init__()

    def __randomize_sleep_time(self):
        inferior_limit = 0.7
        upper_limit = 0.9
        real_num = uniform(inferior_limit, upper_limit)
        return float(f'{real_num:.3}')

    def _start_key_press(self) -> bool:
        keyboard_controller.tap(key_event.initialize)
        time = self.__randomize_sleep_time()
        sleep(time) #O sleep precisa estar depois do .tap(key)
        return True
