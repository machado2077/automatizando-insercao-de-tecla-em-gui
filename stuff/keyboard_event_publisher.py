from .interfaces.keyboard_event_listener import KeyboardEventListenerInterface
from .interfaces.observer import ObserverInterface, ObservableInterface
from threading import Event

class KeyboardEventPublisher(ObservableInterface):
    def __init__(self, listener: KeyboardEventListenerInterface) -> None:
        self.__observers = []
        self.__keyboard_event = None
        listener.listening_keyboard_event = self.listening_keyboard_event
    
    def subscribe(self, observer: ObserverInterface) -> None:
        return self.__observers.append(observer)
    
    def unsubscribe(self, observer: ObserverInterface) -> None:
        if observer in self.__observers:
            self.__observers.remove(observer)

    def notify(self) -> None:
        for observer in self.__observers:
            observer.update(self.__keyboard_event)
    
    def listening_keyboard_event(self, keyboard_event) -> None:
        self.__keyboard_event = keyboard_event
        self.notify()
    
    

    

    