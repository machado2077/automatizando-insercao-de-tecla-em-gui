from abc import ABC, abstractmethod
from . import key_event


class AbstractKeyboardEventResponse(ABC):
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

    @abstractmethod
    def start_key_press(self) -> bool:        
        return True

    def pause_keyboard_press(self) -> bool:
        return True
    
    def finish_keyboard_press(self) -> bool:
        return False
