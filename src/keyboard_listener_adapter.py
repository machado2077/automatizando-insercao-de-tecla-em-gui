from threading import Event
from pynput.keyboard import Listener
from .interfaces.observer import ObservableInterface, ObserverInterface


class PynputKeyboardListenerAdapter(ObservableInterface): 
    def __init__(self) -> None:
        self.__listener = Listener(on_press=self.listen_to_keyboard_events)
        self.__event = Event()
        self.__observers = []
    
    def subscribe(self, observer: ObserverInterface) -> None:
        self.__observers.append(observer)

    def notify(self, keyboard_event):
        for observer in self.__observers:
            observer.update(keyboard_event)

    def handle_keyboard_event(self, keyboard_event):
        key_handled = str(keyboard_event.char).lower()
        return key_handled

    def listen_to_keyboard_events(self, keyboard_event):
        try:
            key_handled = self.handle_keyboard_event(keyboard_event)
            self.__event.set()
        except AttributeError:
            pass        
        else:
            self.__event.clear()
            self.notify(key_handled)        

    def start(self):
        self.__listener.start()
        self.__event.wait()
