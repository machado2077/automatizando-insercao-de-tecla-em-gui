from ..interfaces import IKeyboardEventOutputPort

class KeyboardEventResponse(IKeyboardEventOutputPort):
    """Classe responsável por abstrair as respostas às solicitações referentes aos comandos passados ao MainProcessController, pelo usuário da aplicação. Por fim, retornar ao MainProcessController o feedback dessa solicitação.
    """
    def __init__(self) -> None:
        self.__response_adapter = None
        #TODO: IMPLEMENTAR O MAPEADOR DESSES COMANDOS
        self.responses = {
            'a': self.__start_key_press,
            'q': self.__stop_key_press,
            'f': self.__finish_key_press
        }
        self.__current_response = None

    @property
    def response_adapter(self):
        ...
    
    @response_adapter.setter
    def response_adapter(self, adapter):
        self.__response_adapter = adapter

    def __start_key_press(self) -> bool:
        self.__response_adapter.start_key_press()
        return True
    
    def __stop_key_press(self) -> bool:
        return True
    
    def __finish_key_press(self) -> bool:
        return False

    def respond_to_keyboard_event(self, keyboard_event: str) -> bool:
        response = self.responses.get(keyboard_event)
        if response:
            self.__current_response = response
            return response()
        return self.__current_response()
