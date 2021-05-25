from threading import Lock, Event, Thread
from time import sleep
from pynput import keyboard

START_KEY = 'a'
STOP_KEY = 'q'
TAP_DELAY = 0.5

stop_key_pressed_event = Event()
controller = keyboard.Controller()
lock = Lock()
start_key_pressed_event = Event()

def start_key_pressed(key):
    try:
        if str(key.char).lower() == START_KEY:
            start_key_pressed_event.set()
    except AttributeError:
        pass


def stop_key_pressed(key):
    lock.acquire()
    try:        
        if str(key.char).lower() == STOP_KEY:
            stop_key_pressed_event.set()
    except AttributeError:
        pass
    finally:
        lock.release()
    

def start_key_press():
    while True:
        if stop_key_pressed_event.is_set():
            break
        controller.tap(START_KEY)
        sleep(TAP_DELAY)



start_listener = keyboard.Listener(on_press=start_key_pressed)
start_listener.start()
start_key_pressed_event.wait()

stop_listener = keyboard.Listener(on_press=stop_key_pressed)
stop_listener.start()

start_key_press_thread = Thread(target=start_key_press, daemon=True)
start_key_press_thread.start()

stop_key_pressed_event.wait()