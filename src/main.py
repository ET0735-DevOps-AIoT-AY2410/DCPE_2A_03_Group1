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

scanning = True
adjustment = False
fireDetection = False
tempThres = 40             # Default temperature threshold
lightThres = 170            # Default light threshold

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
    fireDetectionCooldown = False

    init()    # Initialize Components
    start_threads() # Start all necessary detached threads
    
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
                    notification.sendNotif("fire","location")
                    alarm.thread_when_fire_detected()
                    sprinkler.when_fire_detected(fireDetection)
                RetVal = deactivation.rfidThread(fireDetection)
                if (RetVal == 3):
                    print("in false mode")
                    fireDetection = False
                    alarm.stopThread = True         # Stop the alarm thread  
                    deactivation.stopThread = True          # Stop the deactivation thread                                 
                    sprinkler.when_fire_detected(fireDetection)
                    print("test stop alarm thread") 
            else: # !fireDetection
                fireDetectionCooldown == True
            
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
            scanning = True
            adjustment = False
if __name__ == "__main__":
    main()