from threading import Event
from pynput.keyboard import Listener
from ..core.application.interfaces import IKeyboardEventInputPort

class PynputEventListenerAdapter:
    def __init__(self, adaptee: IKeyboardEventInputPort) -> None:
        self.adaptee = adaptee
        self.__event_manager = Event()
        listener = Listener(on_press=self.listen_to_keyboard_events)
        listener.start()
        self.__event_manager.wait()

    def listen_to_keyboard_events(self, keyboard_event) -> None:
        try:
            key = str(keyboard_event.char)
            self.__event_manager.set()
        except AttributeError:
            pass
        else:
            self.__event_manager.clear()
            self.adaptee.update_keyboard_event(key)



def plug_app(app):
    listener_port = app.listener_port
    PynputEventListenerAdapter(listener_port)
