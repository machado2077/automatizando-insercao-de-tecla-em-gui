from threading import Lock, Event, Thread
from time import sleep
from pynput import keyboard

START_KEY = 'a'
STOP_KEY = 'q'
TAP_DELAY = 0.5

stop_key_pressed_event = Event()
start_key_pressed_event = Event()
controller = keyboard.Controller()
lock = Lock()

def key_pressed(key):
    lock.acquire()
    try:        
        if str(key.char).lower() == STOP_KEY:
            stop_key_pressed_event.set()
    except AttributeError:
        pass
    finally:
        lock.release()
    try:
        if str(key.char).lower() == START_KEY:
            start_key_pressed_event.set()
    except AttributeError:
        pass
    
    

def start_key_press():
    while True:
        if stop_key_pressed_event.is_set():
            break
        controller.tap(START_KEY)
        sleep(TAP_DELAY)



key_listener = keyboard.Listener(on_press=key_pressed)
key_listener.start()
start_key_pressed_event.wait()

'''
estratégia:
- se a tecla A for acionada, um evento estoura e permite que a tecla 'a' seja acionada
- se a tecla Q for acionada, um eventou estoura e finaliza o processo

'''


start_key_press_thread = Thread(target=start_key_press, daemon=True)
start_key_press_thread.start()

stop_key_pressed_event.wait()