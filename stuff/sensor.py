from abc import ABC, abstractmethod

class AbstractKeyBoardSensor(ABC):
    def __init__(self) -> None:
        self._key_pressed = None

    @property
    def key_pressed(self) -> str:
        self._key_pressed = self.get_user_triggered_key()
        return self._key_pressed

    @abstractmethod
    def get_user_triggered_key(self) -> str: 
        ...



from pynput.keyboard import Listener
class PynputKeyBoardListener:
    #TODO: IMPLEMENTAR UM GETTER
    def __init__(self) -> None:
        self.sinal = None
        self.listener = None
    
    def ouvindo_tecla(self, key):
        if self.listener:
            try:
                self.sinal = str(key.char).lower()
            except AttributeError:
                pass
            #return self.sinal

    def inicializar(self):
        if not self.listener:
            self.l = Listener(self.ouvindo_tecla)
            self.l.start()

    