import time
from threading import Thread, Event
import alarm
import detection
import deactivation
import notification
import sos_switch as sos
import sprinkler
import hmi as menu
import queue

shared_keypad_queue = queue.Queue()
scanning = True
adjustment = False
alarm_thread = None
alarm_thread_event = Event()

def key_pressed(key):
    shared_keypad_queue.put(key)

def alarm_thread_function():
    while not alarm_thread_event.is_set():
        alarm.when_fire_detected()

def main():
    # Initialize Components
    alarm.init()
    detection.init()
    sprinkler.init()
    sos.init()
    menu.init()
    
    # Start Threads
    sos_thread = Thread(target=sos.switchON)
    sos_thread.start()

    global alarm_thread
    alarm_thread_event.clear()

    while True:
        while(scanning):
            menu.scannerMode()

            keyvalue = shared_keypad_queue.get()
            if(keyvalue == 0):                  #if keypad '0' pressed, switch to adjustment system             
                scanning = False
                adjustment = True

            fireDetection = detection.alarmStatus()
            print(fireDetection)
            if fireDetection:
                notification.sendNotif("fire","location")
                notification.sendNotif("help","location")

                if alarm_thread is None or not alarm_thread.is_alive():
                    alarm_thread_event.clear()
                    alarm_thread = Thread(target=alarm_thread_function)
                    alarm_thread.start()
                sprinkler.when_fire_detected(fireDetection)
            else:
                if alarm_thread and alarm_thread.is_alive():
                    alarm_thread_event.set()
                    alarm_thread.join()  # Wait for the thread to finish

                sos.isSwitchON()

        while(adjustment):                #go back to scanner after adjusting threshold
            menu.adjustMode()
            scanning = True
            adjustment = False

if __name__ == "__main__":
    main()