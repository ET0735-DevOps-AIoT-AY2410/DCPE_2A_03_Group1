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

fireDetection = False

def main():
    # Initialize Components
    alarm.init()
    detection.init()
    sprinkler.init()
    sos.init()
    menu.init()
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