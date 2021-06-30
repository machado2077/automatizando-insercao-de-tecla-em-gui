from ..core.application.interfaces import IKeyboardEventOutputPort

class KeyboardEventResponse(IKeyboardEventOutputPort):
    """Classe responsável por abstrair as respostas referentes aos comandos passados ao MainProcessController pelo usuário da aplicação.
    """
    def __init__(self) -> None:
        self.__response_adapter = None
        self.responses = {
            'a': self.start_key_press
        }

    @property
    def response_adapter(self):
        ...
    
    @response_adapter.setter
    def response_adapter(self, adapter):
        self.__response_adapter = adapter

    def start_key_press(self):
        self.__response_adapter.start_key_press()
        return True

    def respond_to_keyboard_event(self, keyboard_event: str) -> bool:
        #TODO: TRATAR CASO O COMANDO NÃO EXISTA, DE MODO A CONTINUAR O PROCESSO ANTERIOR CASO UM TECLA NÃO EXISTENTE FOR ACIONADA
        response = self.responses.get(keyboard_event)
        if response:            
            response()
        return True