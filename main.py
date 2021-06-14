from src import MainProcessController, PynputKeyboardListener, PynputKeyboardEventResponse


key_listener_adapter = PynputKeyboardListener()
keyboard_event_response = PynputKeyboardEventResponse()
proc_controller = MainProcessController(keyboard_event_response)

key_listener_adapter.subscribe(proc_controller)

if __name__ == "__main__":
    key_listener_adapter.start()
    proc_controller.start_main_process()
