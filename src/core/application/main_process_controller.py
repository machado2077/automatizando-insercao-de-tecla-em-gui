from .interfaces import IKeyboardEventOutputPort
from time import sleep

class MainProcessController:
    """Classe responsável por controlar o loop principal
    """
    def __init__(self, responsable: IKeyboardEventOutputPort) -> None:
        self.__responsable = responsable
        self.__keyboard_event = None

    def update_keyboard_event(self, keyboard_event: str) -> None:
        self.__keyboard_event = keyboard_event

    def __main_process(self) -> None:
        while True:
            process = self.__responsable.respond_to_keyboard_event(
                self.__keyboard_event
                )
            if process == False:
                return

    def start_main_process(self) -> None:
        self.__main_process()
