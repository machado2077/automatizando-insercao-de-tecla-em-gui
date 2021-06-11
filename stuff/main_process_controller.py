from pynput.keyboard import Controller
from .interfaces.keyboard_event_listener import KeyboardEventListenerInterface

"""
- o controller deve ser notificado a cada novo -evento e processar
- a cada novo evento mapeado o seu processo interno é alterado
- deve haver alguma forma de saber o estado para ver ser está sendo teclado algo

#TODO: testar o processamento da entrada
#TODO: fazer as funções de comandos de parar_de_teclar, começar_teclar, finalizar
#TODO: analisar se a função "sincrona" do proc_controller funciona para os dois processos (finalizar e atuar)


processos:
iniciado: não faz nada
finalizar: finalizar
apertar: apertar
pausar: pausar
"""

from threading import Thread
from pynput.keyboard import Controller
from time import sleep

c = Controller()

class MainProcessController(KeyboardEventListenerInterface):
    def __init__(self, listener: KeyboardEventListenerInterface) -> None:
        self.current_process = None
        self.listener = listener
        listener.process_keyboard_event = self.process_keyboard_event
        self.__process = True

    #MÉTODOS A SEREM ABSTRAÍDOS --------
    def continue_main_process(self):
        if self.current_process:
            self.current_process()
    
    def finish_process(self):
        self.__process = False
    
    def start_key_press(self):
        c.tap('a')
        sleep(0.8)

    def stop_key_press(self):
        ...
    #------------------
    def update(self, keyboard_event):
        """
        existem duas formas: 
        - receber o processo do key_event_response, validar se há uma método a ser executado (é oq é feito atualmente) -> essa forma pressupõe que seja enviado o "guardador do processo (estado)" para o key_event_response para que esse atributo seja alterado em outra classe: indesejado

        - enviar o evento para o key_event_response, que irá executar "na sua classe" o procedimento e retornar um bool. Em seguida, o controlador irá validar se o retorno é verdadeiro ou falso
        """
        ...

    def main_process(self):
        """
        while True:
            self.process = key_response.handle_keyboard_event()
            if not self.process:
                return
        """
        while self.__process:
            self.continue_main_process()

    def start_main_process(self):
        self.listen_to_keyboard_events()
        self.main_process()

    def process_keyboard_event(self, keyboard_event) -> None:
        #TODO: TORNAR ISSO UMA RESPONSABILIDADE DO keyboard_event_response 
        if keyboard_event == 'f':
            self.current_process = self.finish_process
        elif keyboard_event == 'a':
            self.current_process = self.start_key_press
        elif keyboard_event == 'q':
            self.current_process = self.stop_key_press

    def listen_to_keyboard_events(self):
        self.listener.start()