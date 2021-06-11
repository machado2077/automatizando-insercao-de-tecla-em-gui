class Actuator:
    def __init__(self) -> None:
        self._key_pressed = None
    
    def start_key_press(self):
        if self._key_pressed:
            ...