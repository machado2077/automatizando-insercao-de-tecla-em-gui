import os
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
        self.__current_command = {"input": None, "response_method": lambda: True, "new": True}

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
    
    def __clear_shell(self):
        os.system("cls" if os.name == "nt" else "clear")

    def __response_method(self):
        return self.__current_command.get("response_method")()

    def __handle_response(self):
        if not self.__current_command.get("new"):
            return self.__response_method()
        command = self.__current_command.get("input")
        if command == "a":
            print("INICIADO\n")
        elif command == "q":
            print("PAUSADO\n")
        elif command == "f":
            print("FINALIZADO\n")
        self.__current_command.update(new=False)
        return self.__response_method()

    def respond_to_keyboard_event(self, keyboard_event: str) -> bool:
        response = self.responses.get(keyboard_event)
        if response:
            if not keyboard_event == self.__current_command.get("input"):
                self.__current_command.update(
                    input=keyboard_event,
                    response_method=response,
                    new=True
                )
                self.__clear_shell()
            return self.__handle_response()
        return self.__response_method()

"""
PROBLEMAS:
- as respostas não estão mapeadas (tudo hardcoded)
- comparações de IF para printar a mensagem do comando

SOLUÇÕES:
- como relacionar o mapeamento dos comandos de respostas com o comando atual:
    - colocar o mapeamento de respostas dentro do comando atual
- o que seria o mapeamento de comandos?:
    - seria um mapeamento que teria acesso as configurações dos comandos do usuário
    - teria uma relação, para cada comando:
        tecla - comando - mensagem
    - como iniciar?

"""