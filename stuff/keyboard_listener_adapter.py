from threading import Event
from queue import Queue
from pynput.keyboard import Listener
from .interfaces.keyboard_event_listener import KeyboardEventListenerInterface

class PynputKeyboardListenerAdapter(KeyboardEventListenerInterface):
    def __init__(self) -> None:
        self.listener = Listener(on_press=self.receive_keyboard_event)
        self.listener.start()
        self.event = Event()
        self.event.wait()
        

    def handle_keyboard_event(self, keyboard_event):
        key_handled = str(keyboard_event.char).lower()
        return key_handled

    def receive_keyboard_event(self, keyboard_event):
        try:
            key_handled = self.handle_keyboard_event(keyboard_event)
            self.event.set()
        except AttributeError:
            pass        
        else:
            self.event.clear()
            self.listening_keyboard_event(key_handled)
    
    def listening_keyboard_event(self, keyboard_event):
        ...
