from threading import Lock, Event, Thread
from time import sleep
from pynput import keyboard

START_KEY = 'a'
STOP_KEY = 'q'


stop_key_pressed_event = Event()
controller = keyboard.Controller()
lock = Lock()
TIMEOUT_WAIT_SECONDS = 600  #10 MINUTES
TAP_DELAY = 0.5

def stop_key_pressed(key):
    lock.acquire()
    try:        
        if str(key.char).lower() == STOP_KEY:
            print('parou')
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

sleep(3)


stop_listener = keyboard.Listener(on_press=stop_key_pressed)
stop_listener.start()

start_key_press_thread = Thread(target=start_key_press, daemon=True)
start_key_press_thread.start()
stop_key_pressed_event.wait(TIMEOUT_WAIT_SECONDS)


