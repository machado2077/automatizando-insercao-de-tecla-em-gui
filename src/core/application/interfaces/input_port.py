from abc import ABC, abstractmethod


class IKeyboardEventInputPort(ABC):
    @abstractmethod
    def update_keyboard_event(self): 
        ...