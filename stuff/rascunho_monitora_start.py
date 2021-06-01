from threading import Event
from pynput import keyboard

START_KEY = 'a'

start_key_pressed_event = Event()

def start_key_pressed(key):
    try:
        if str(key.char).lower() == START_KEY:
            print('startou')
            start_key_pressed_event.set()
    except AttributeError:
        pass
    
start_listener = keyboard.Listener(on_press=start_key_pressed)
start_listener.start()
start_key_pressed_event.wait()

"""
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
"""