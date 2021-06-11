from abc import ABC, abstractmethod

class KeyboardEventListenerInterface(ABC):

    @abstractmethod
    def listen_to_keyboard_events(self):
        ...

    @abstractmethod
    def process_keyboard_event(self):
        ...