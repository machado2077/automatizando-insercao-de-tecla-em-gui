from ..core.application.interfaces import IKeyboardEventInputPort
from ..core.application import MainProcessController


class KeyboardEventListener(IKeyboardEventInputPort):
    def __init__(self, proc_controller: MainProcessController) -> None:
        self.__proc_controller = proc_controller
    
    def update_keyboard_event(self, keyboard_event):
        self.__proc_controller.update_keyboard_event()
    
    def __handle_keyboard_event(self, keyboard_event: str) -> str:
        key_handled = str(keyboard_event).lower()
        return key_handled
