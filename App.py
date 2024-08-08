import time
from threading import Thread, Event
from src import alarm
from src import detection
from src import deactivation
from src import notification
from src import sos_switch as sos
from src import sprinkler
from src import hmi as menu
import queue
from hal import hal_keypad as keypad

shared_keypad_queue = queue.Queue()
alarm_thread = None
alarm_thread_event = Event()

fireDetection = False



def key_pressed(key):
    shared_keypad_queue.put(key)

def alarm_thread_function():
    
    while not alarm_thread_event.is_set():
        alarm.when_fire_detected(fireDetection)

def main():
    # Initialize Components
    alarm.init()
    detection.init()
    sprinkler.init()
    sos.init()
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

    scanning = True
    adjustment = False
    
    #sos.threadStartSOS()

    # Start Threads

    global alarm_thread
    alarm_thread_event.clear()

    while True:
        while(scanning):
            menu.scannerModeThread()

            try:
                keyvalue = shared_keypad_queue.get_nowait()
            except queue.Empty:
                keyvalue = None
            #keyvalue = shared_keypad_queue.get_nowait()
            print("test hello")
            print(keyvalue)

            if(keyvalue == 0):                  #if keypad '0' pressed, switch to adjustment system             
                scanning = False
                adjustment = True
            
            fireDetection = detection.alarmStatus()
            print("test alarm")
            print(fireDetection)
            if fireDetection:
                print("in fire mode")
                #notification.sendNotif("fire","location")
                #time.sleep(1)
                #notification.sendNotif("help","location")

                if alarm_thread is None or not alarm_thread.is_alive():
                    alarm_thread_event.clear()
                    alarm_thread = Thread(target=alarm_thread_function)
                    alarm_thread.start()
                sprinkler.when_fire_detected(fireDetection)
            else:
                if alarm_thread and alarm_thread.is_alive():
                    alarm_thread_event.set()
                    alarm_thread.join()  # Wait for the thread to finish

                

        while(adjustment):                #go back to scanner after adjusting threshold
            menu.adjustMode()
            scanning = True
            adjustment = False

if __name__ == "__main__":
    main()