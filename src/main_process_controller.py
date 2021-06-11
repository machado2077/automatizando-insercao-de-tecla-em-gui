from .interfaces.keyboard_event_listener import KeyboardEventListenerInterface
from .interfaces.observer import ObserverInterface

"""
- o controller deve ser notificado a cada novo evento e processar;
- a cada novo evento mapeado o seu processo interno é alterado;
- deve haver alguma forma de saber o estado para ver ser está sendo teclado algo
"""

class MainProcessController2(ObserverInterface):
    def __init__(self, keyboard_event_response) -> None:
        self.keyboard_event_response = keyboard_event_response
        self.__keyboard_event = None
    
    def update(self, keyboard_event):
        self.__keyboard_event = keyboard_event

    def main_process(self):
        while True:
            process = self.keyboard_event_response.respond_to_keyboard_event(self.__keyboard_event)
            if process == False:
                return

    def start_main_process(self):
        self.main_process()



class MainProcessController(KeyboardEventListenerInterface):
    def __init__(self, listener: KeyboardEventListenerInterface, keyboard_event_response) -> None:
        self.listener = listener
        self.keyboard_event_response = keyboard_event_response
        self.__keyboard_event = None

    def main_process(self):
        while True:
            process = self.keyboard_event_response.respond_to_keyboard_event(self.__keyboard_event)
            if process == False:
                return

    def start_main_process(self):
        self.listener.process_keyboard_event = self.process_keyboard_event
        self.listen_to_keyboard_events()
        self.main_process()

    def process_keyboard_event(self, keyboard_event) -> None:
        self.__keyboard_event = keyboard_event

    def listen_to_keyboard_events(self):
        self.listener.start()