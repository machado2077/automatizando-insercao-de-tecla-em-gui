from .interfaces.observer import ObserverInterface
from .abstract_classes.abstract_keyboard_event_response import AbstractKeyboardEventResponse


class MainProcessController(ObserverInterface):
    def __init__(self, response: AbstractKeyboardEventResponse) -> None:
        self.__response = response
        self.__keyboard_event = None
    
    def update(self, keyboard_event: str) -> None:
        self.__keyboard_event = keyboard_event

    def __main_process(self) -> None:
        while True:
            process = self.__response.respond_to_keyboard_event(
                self.__keyboard_event
                )
            if process == False:
                return

    def start_main_process(self) -> None:
        self.__main_process()
