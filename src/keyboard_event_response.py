from .keyboard_event_mapper import keyboard_event_mapper as key_event

from pynput.keyboard import Controller
from time import sleep

keyboard_controller = Controller()
#TODO: fazer uma classe abstrata que vai passar o init e o respond_to_keyboard_event

class KeyboardEventResponse:
    def __init__(self) -> None:
        self.responses = {
            key_event.initialize: self.start_key_press,
            key_event.pause: self.pause_keyboard_press,
            key_event.finish: self.finish_keyboard_press
        }

    def respond_to_keyboard_event(self, keyboard_event: str) -> bool:
        response = self.responses.get(keyboard_event)
        if response:
            return response()
        return True
    
    def start_key_press(self) -> bool:
        keyboard_controller.tap(key_event.initialize)
        sleep(0.8) #O sleep precisa estar depois do .tap(key)
        return True
    
    def pause_keyboard_press(self) -> bool:
        return True
    
    def finish_keyboard_press(self) -> bool:
        return False
