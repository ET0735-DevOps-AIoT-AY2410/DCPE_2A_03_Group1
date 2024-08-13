import time
from threading import Thread, Event
import queue
from hal import hal_keypad as keypad

# Global variables
shared_keypad_queue = queue.Queue()
keyPressed = Event()
keyvalue = None

def key_pressed(key):
    global keyvalue
    keyvalue = key
    keyPressed.set()
    shared_keypad_queue.put(key)

def keypad_thread_func():
    keypad.init(key_pressed)
    while True:
        keypad.get_key()
        time.sleep(0.1)  # Small delay to avoid high CPU usage

def keypadThread():
    thread = Thread(target=keypad_thread_func)
    thread.daemon = True
    thread.start()
