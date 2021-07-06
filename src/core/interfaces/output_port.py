from abc import ABC, abstractmethod


class IKeyboardEventOutputPort(ABC):
    @abstractmethod
    def respond_to_keyboard_event(self):
        ...