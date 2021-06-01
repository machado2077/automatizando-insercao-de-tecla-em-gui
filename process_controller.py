from response import response


class ProcessController:

    def __init__(self, sensor, actuator) -> None:
        self.sensor = sensor
        self.actuator = actuator
        #__keyboard_event PRECISA EXISTIR PARA GUARDAR A TECLA DO "INSTANTE" A SER PROCESSADA
        self.__keyboard_event = None

    @property
    def keyboard_event(self) -> str:
        return self.__keyboard_event    

    def get_keyboard_event(self) -> None:
        self.__keyboard_event = self.sensor.key_pressed

    def process_keyboard_events(self) -> None:
        while True:
            self.get_keyboard_event()
            if self.keyboard_event == response.finish:
                break
            self.send_keyboard_event_to_actuator()
            
    def send_keyboard_event_to_actuator(self) -> None:
        #Preciso desse método sem parâmetro para poder realizar testes de integração
        self.actuator.respond_to_keyboard_event(self.keyboard_event)

