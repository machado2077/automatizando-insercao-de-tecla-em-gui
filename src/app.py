from .core.application import MainProcessController
from .ports import KeyboardEventListener, KeyboardEventResponse

class App:
    """Classe responsável por estabelecer as portas de acesso ao MainProcessController, retornando um objeto que incorpora a aplicação desejada. Essas portas serão acessadas por adaptadores que irão implementar os casos de uso para o funcionamento da aplicação, utilizando de recursos externos.
    """
    def __init__(self) -> None:
        self.response_port = KeyboardEventResponse()
        self.__controller = MainProcessController(self.response_port)
        self.listener_port = KeyboardEventListener(self.__controller)
    
    def run(self) -> None:
        self.__controller.start_main_process()
