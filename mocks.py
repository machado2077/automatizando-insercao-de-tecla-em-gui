from sensor import AbstractKeyBoardSensor
from response import response


class SensorMock(AbstractKeyBoardSensor):
    def __init__(self) -> None:
        super().__init__()
        self._keyboard_listener = None

    def handle_keyboard_event_output(self, key):
        return str(key).lower()

    def get_user_triggered_key(self) -> str:
        if self._keyboard_listener:
            key = self._keyboard_listener.key
            return self.handle_keyboard_event_output(key)



class ListenerMock:
    def __init__(self) -> None:
       self._key = None
    
    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, value):
        self._key = value



class ListenerMockLazy(ListenerMock):
    CALL_LIMIT = 5

    def __init__(self) -> None:
        super().__init__()
        self.count = 0
        
    @property
    def key(self):
        if self.count == 0:
            self._key = response.initialize
        if self.count == self.CALL_LIMIT:
            self._key = response.finish
            return self._key
        self.count += 1
        return self._key
    


class ListenerMockNone(ListenerMockLazy):
    def __init__(self) -> None:
        super().__init__()
        self.count = 0        

    @property
    def key(self):
        if self.count == self.CALL_LIMIT:
            return response.finish
        self.count += 1
        return self._key



class ActuatorMock:
    def respond_to_keyboard_event(self, key_pressed: str) -> None:
        if key_pressed == response.initialize:
            self.start_key_press()
        elif key_pressed == response.pause:
            self.stop_key_press()

    def stop_key_press(self): 
        ...

    def start_key_press(self):
        ...
