import os
from ..interfaces import IKeyboardEventOutputPort
from ..keyboard_command_mapper import key_mapper
from ..keyboard_command_response import Response

class KeyboardEventResponse(IKeyboardEventOutputPort):
    """Classe responsável por receber os comandos do usuário, tratar e implementar as respostas da aplicação e certificar o retorno adequado ao controlador principal do processo."""
    def __init__(self) -> None:
        self.__response_adapter = None
        RESPONSES_MAPPED_ARGS = {
            "init_method":self.__start_key_press,
            "pause_method":self.__stop_key_press,
            "finish_method":self.__finish_key_press
        }
        self.__responses = self._response_mapper(**RESPONSES_MAPPED_ARGS)
        self.__current_command_name = None

    def respond_to_keyboard_event(self, keyboard_event: str) -> bool:
        response = bool(self.__get_response(keyboard_event))
        if response:
            return self.__handle_response(keyboard_event)
        current_response = self.__get_response(self.__current_command_name)
        if bool(current_response):
            return current_response.method()
        return True

    def __get_response(self, command: str) -> Response:
        return self.__responses.get(command)

    def __handle_response(self, command: str) -> bool:
        response = self.__get_response(command)
        if command == self.__current_command_name:
            return response.method()
        self.__current_command_name = command
        self.__handle_user_response_message()
        return response.method()

    def __handle_user_response_message(self) -> None:
        self.__clear_shell()
        response = self.__get_response(self.__current_command_name)
        response.message()

    def __clear_shell(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
    
    def _response_mapper(self, init_method, pause_method, finish_method) -> dict:
        print_msg = lambda msg: lambda: print(f"{msg}\n")
        mapper = {
            key_mapper.initialize: Response(init_method, print_msg("INICIADO") ),
            key_mapper.pause: Response(pause_method, print_msg("PAUSADO")),
            key_mapper.finish: Response(finish_method, print_msg("FINALIZADO"))
        }
        print('APERTE PARA COMEÇAR')
        return mapper

    @property
    def response_adapter(self):
        ...
    
    @response_adapter.setter
    def response_adapter(self, adapter):
        self.__response_adapter = adapter

    #IMPLEMENTAÇÕES DE RESPOSTA DA APLICAÇÃO E RETORNO AO CONTROLADOR PRINCIPAL
    def __start_key_press(self) -> bool:
        self.__response_adapter.start_key_press()
        return True
    
    def __stop_key_press(self) -> bool:
        return True
    
    def __finish_key_press(self) -> bool:
        return False
