import json
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
import keypad

def load_thresholds():
    global tempThres, lightThres
    with open('thresholds.json', 'r') as file:
        thresholds = json.load(file)
        tempThres = thresholds['tempThres']
        lightThres = thresholds['lightThres']

def save_thresholds():
    thresholds = {
        'tempThres': tempThres,
        'lightThres': lightThres
    }
    with open('thresholds.json', 'w') as file:
        json.dump(thresholds, file)

global scanning, adjustment, fireDetection, tempThres, lightThres
scanning = True
adjustment = False
fireDetection = False
tempThres = 99
lightThres = 171
load_thresholds()

def init():                # Initialize Components
    alarm.init()
    detection.init()
    sprinkler.init()
    sos.init()
    menu.init()

def start_threads():              # Start all necessary detached threads
    sos.thread_isSwitchON()
    keypad.keypadThread()

def main():
    global scanning, adjustment, fireDetection, tempThres, lightThres

    init()    # Initialize Components
    start_threads() # Start all necessary detached threads
    
    time.sleep(1)
    fireDetectionCooldown = False

    while True:
        # SCANNING MODE
        while(scanning):
            print ("entered scanning")
            menu.scannerMode()
            if detection.alarmStatus() == True:         # Check if fire detected, once detected once, alarm continues to sound until deactivated
                fireDetection = True

            if fireDetection:
                if fireDetectionCooldown == False: # this cooldown is so that it only sends notif ONCE
                    fireDetectionCooldown = True
                    notification.sendNotif("fire","123456 Dover Road")
                    alarm.thread_when_fire_detected()
                    sprinkler.when_fire_detected(True) # 180
                RetVal = deactivation.rfidThread(fireDetection)
                if (RetVal == 3):
                    print("in false mode")
                    fireDetection = False
                    alarm.stopThread = True         # Stop the alarm thread  
                    deactivation.stopThread = True          # Stop the deactivation thread                                 
                    sprinkler.when_fire_detected(False) # 0
                    print("test stop alarm thread") 
            
            try:
                if keypad.shared_keypad_queue.get_nowait() == '*':  # If keypad '*' pressed, switch to adjustment system
                    scanning = False
                    adjustment = True
            except queue.Empty:
                pass
                
        # ADJUSTMENT MODE
        while(adjustment): # go back to scanner after adjusting threshold               
            print ("entered adjustment")
            menu.adjustMode()
            save_thresholds()
            scanning = True
            adjustment = False

if __name__ == "__main__":
    main()
    