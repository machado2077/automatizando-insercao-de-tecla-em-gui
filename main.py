from src import KeyboardEventResponse, MainProcessController, PynputKeyboardListenerAdapter



keyboard_event_response = KeyboardEventResponse()
"""
key_listener_adapter = PynputKeyboardListenerAdapter()

proc_controller = MainProcessController(key_listener_adapter, keyboard_event_response)
"""
from src.main_process_controller import MainProcessController2
from src.keyboard_listener_adapter import PynputKeyboardListenerAdapter2

proc_controller = MainProcessController2(keyboard_event_response)
key_listener_adapter = PynputKeyboardListenerAdapter2()
key_listener_adapter.subscribe(proc_controller)
key_listener_adapter.start()


if __name__ == "__main__":
    proc_controller.start_main_process()