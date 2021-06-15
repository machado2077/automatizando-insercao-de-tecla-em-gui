
class PynputEventListenerAdapter:
    def __init__(self, event_manager, port):
        self.__event_manager = event_manager
        self.__port = port

    def listen_to_keyboard_events(self, keyboard_event) -> None:
        try:
            key_handled = self.__handle_keyboard_event(keyboard_event)
            self.__event.set()
        except AttributeError:
            pass
        else:
            self.__event.clear()
            self.__send_keyboard_event(key_handled)

    def __handle_keyboard_event(self, keyboard_event) -> str:
        return str(keyboard_event.char)

    def __send_keyboard_event(self, keyboard_event):
        self.__port.update_keyboard_event(keyboard_event)
