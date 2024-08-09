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
from hal import hal_keypad as keypad

def init():
    alarm.init()
    detection.init()
    sprinkler.init()
    sos.init()
    menu.init()

def start_threads():
    sos.thread_isSwitchON()
    alarm.thread_when_fire_detected()

def main():
    init() # Initialize Components
    start_threads() # Start all necessary detached threads

    global scanning, fireDetection
    scanning = True
    fireDetection = False

    while True:
        # SCANNING MODE
        while(scanning):
            menu.thread_scannerMode()
            print("test scanner")   
            
            fireDetection = detection.alarmStatus()
            print("test alarm Status")
            print(fireDetection)
            print("test fire detection")
            if fireDetection:
                print("in fire mode")
                notification.sendNotif("fire","location")
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

            if(keyvalue == 0):                  #if keypad '0' pressed, switch to adjustment system             
                scanning = False
                adjustment = True
        # ADJUSTMENT MODE
        while(adjustment):                #go back to scanner after adjusting threshold
            menu.adjustMode()
            scanning = True
            adjustment = False

if __name__ == "__main__":
    main()