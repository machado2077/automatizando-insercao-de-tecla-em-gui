from ..core.application.interfaces import IKeyboardEventOutputPort


class KeyboardEventResponse(IKeyboardEventOutputPort):
    def __init__(self) -> None:
        self.responses = {
            
        }

    def respond_to_keyboard_event(self, keyboard_event: str) -> bool:
        response = self.responses.get(keyboard_event)
        if response:
            return response()
        return True