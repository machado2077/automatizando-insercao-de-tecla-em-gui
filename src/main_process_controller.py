from .interfaces.observer import ObserverInterface
from .abstract_classes.abstract_keyboard_event_response import AbstractKeyboardEventResponse


class MainProcessController(ObserverInterface):
    def __init__(self, responsible: AbstractKeyboardEventResponse) -> None:
        self.responsible = responsible
        self.__keyboard_event = None
    
    def update(self, keyboard_event):
        self.__keyboard_event = keyboard_event

    def main_process(self):
        while True:
            process = self.responsible.respond_to_keyboard_event(self.__keyboard_event)
            if process == False:
                return

    def start_main_process(self):
        self.main_process()
