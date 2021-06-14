from threading import Event
from typing import Any
from pynput.keyboard import Listener
from .interfaces.observer import ObservableInterface, ObserverInterface


class PynputKeyboardListener(ObservableInterface): 
    def __init__(self) -> None:
        self.__listener = Listener(on_press=self.__listen_to_keyboard_events)
        self.__event = Event()
        self.__observers = []
    
    def subscribe(self, observer: ObserverInterface) -> None:
        self.__observers.append(observer)

    def notify(self, keyboard_event: str) -> None:
        for observer in self.__observers:
            observer.update(keyboard_event)

    def __handle_keyboard_event(self, keyboard_event: Any) -> str:
        key_handled = str(keyboard_event.char).lower()
        return key_handled

    def __listen_to_keyboard_events(self, keyboard_event: Any) -> None:
        try:
            key_handled = self.__handle_keyboard_event(keyboard_event)
            self.__event.set()
        except AttributeError:
            pass        
        else:
            self.__event.clear()
            self.notify(key_handled)        

    def start(self) -> None:
        self.__listener.start()
        self.__event.wait()
