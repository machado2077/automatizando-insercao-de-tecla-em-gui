from ..interfaces import IKeyboardEventInputPort
from ..main_process_controller import MainProcessController

class KeyboardEventListener(IKeyboardEventInputPort):
    """Classe responsável por abstrair o recebimento dos comandos fornecidos pelo usuário da aplicação, tratar o comando e passá-lo para o MainProcessController.
    """
    def __init__(self, proc_controller: MainProcessController) -> None:
        self.__proc_controller = proc_controller
    
    def update_keyboard_event(self, keyboard_event: str) -> None:
        key_handled = self.__handle_keyboard_event(keyboard_event)
        self.__proc_controller.update_keyboard_event(key_handled)
    
    def __handle_keyboard_event(self, keyboard_event: str) -> str:
        key_handled = str(keyboard_event).lower()
        return key_handled
