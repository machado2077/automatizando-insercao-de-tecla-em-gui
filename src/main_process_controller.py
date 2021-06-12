from .interfaces.observer import ObserverInterface


class MainProcessController(ObserverInterface):
    def __init__(self, keyboard_event_response) -> None:
        self.keyboard_event_response = keyboard_event_response
        self.__keyboard_event = None
    
    def update(self, keyboard_event):
        self.__keyboard_event = keyboard_event

    def main_process(self):
        while True:
            process = self.keyboard_event_response\
                .respond_to_keyboard_event(self.__keyboard_event)
            if process == False:
                return

    def start_main_process(self):
        self.main_process()
