from abc import ABC, abstractmethod
from . import key_event


class AbstractKeyboardEventResponse(ABC):
    def __init__(self) -> None:
        self.responses = {
            key_event.initialize: self._start_key_press,
            key_event.pause: self._pause_keyboard_press,
            key_event.finish: self._finish_keyboard_press
        }

    def respond_to_keyboard_event(self, keyboard_event: str) -> bool:
        response = self.responses.get(keyboard_event)
        if response:
            return response()
        return True

    @abstractmethod
    def _start_key_press(self) -> bool:        
        return True

    def _pause_keyboard_press(self) -> bool:
        return True
    
    def _finish_keyboard_press(self) -> bool:
        return False
