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

fireDetection = False

def key_pressed(key):
    shared_keypad_queue.put(key)

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
    
    sos.threadStartSOS()
    # Start Alarm Thread
    alarm.alarmThread()

    while True:
        menu.adjustMode()
        print("test adjust")
           #adjustment mode
        while(scanning):
            menu.scannerModeThread()            #scanner mode
            print("test scanner")   
            
            fireDetection = detection.alarmStatus()
            print("test alarm Status")
            print(fireDetection)
            print("test fire detection")
            if fireDetection:
                print("in fire mode")
                notification.sendNotif("fire","location")
                notification.sendNotif("help","location")
                print("test notification")

                alarm.alarm_thread_event.set()  # Start the alarm thread
                print("test alarm thread")
                sprinkler.when_fire_detected(fireDetection)
                print("test sprinkler")
                #deactivation.false_alarm()
            else:
                print("in false mode")
                alarm.alarm_thread_event.clear() # Stop the alarm thread
                print("test stop alarm thread")
                #deactivation.false_alarm()

                


            
            

if __name__ == "__main__":
    main()