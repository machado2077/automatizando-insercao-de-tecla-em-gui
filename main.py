from src import MainProcessController, PynputKeyboardListenerAdapter, PynputKeyboardEventResponse


key_listener_adapter = PynputKeyboardListenerAdapter()
keyboard_event_response = PynputKeyboardEventResponse()
proc_controller = MainProcessController(keyboard_event_response)

key_listener_adapter.subscribe(proc_controller)
key_listener_adapter.start()


if __name__ == "__main__":
    proc_controller.start_main_process()
