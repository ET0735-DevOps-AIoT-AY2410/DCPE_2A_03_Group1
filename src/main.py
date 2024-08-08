import time
from threading import Thread
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

def key_pressed(key):
    shared_keypad_queue.put(key)

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

    alarm_thread = Thread(target=alarm.when_fire_detected)

    while True:
        while(scanning):
            menu.scannerMode()
            keyvalue = shared_keypad_queue.get()
            if(keyvalue == 0):                         #if keypad '0' pressed, switch to adjustment system             
                scanning = False
                adjustment = True

            detection.avgTemp()
            print(detection.average_temp)
            detection.alarmStatus()
            if detection.fireDetected == True:
                notification.sendNotif("fire","")
                notification.sendNotif("help","")
                alarm_thread.start()
                sprinkler.when_fire_detected(detection.fireDetected)


            elif detection.fireDetected == False:
                sos.isSwitchON()

        while(adjustment):                #go back to scanner after adjusting threshold
            menu.adjustMode()
            scanning = True
            adjustment = False

if __name__ == "__main__":
    main()