from time import sleep
from pynput.keyboard import Controller
from .keyboard_event_mapper import keyboard_event_mapper as key_event
from .abstract_classes.abstract_keyboard_event_response import AbstractKeyboardEventResponse

keyboard_controller = Controller()


class KeyboardEventResponse(AbstractKeyboardEventResponse):
    def __init__(self) -> None:
        super().__init__()

    def start_key_press(self) -> bool:
        keyboard_controller.tap(key_event.initialize)
        sleep(0.8) #O sleep precisa estar depois do .tap(key)
        return True
