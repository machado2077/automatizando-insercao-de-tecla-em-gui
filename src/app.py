from .core.main_process_controller import MainProcessController
from .core.ports import KeyboardEventListener, KeyboardEventResponse

class App:
    """Classe responsável por estabelecer as portas de acesso aos adapters, retornando um objeto que incorpora a aplicação desejada.
    """
    def __init__(self) -> None:
        self.response_port = KeyboardEventResponse()
        self.__controller = MainProcessController(self.response_port)
        self.listener_port = KeyboardEventListener(self.__controller)
    
    def run(self) -> None:
        self.__controller.start_main_process()
