import time
from threading import Thread
import alarm
import detection
import deactivation
import notification
import sos_switch
import sprinkler
import mainMenu as menu

def main():
    # Initialize Components
    alarm.init()
    detection.init()
    sprinkler.init()
    sos_switch.init()
    menu.init()
    
    # Start Threads
    sos_thread = Thread(target=sos_switch.switchON)
    sos_thread.start()

    menu_thread = Thread(target=menu.start)
    menu_thread.start()

    # Main Loop
    while True:
        detection.pingtemp()
        detection.pingadc()
        detection.avgTemp()
        detection.alarmStatus()
        if detection.fireDetected:
            alarm.when_fire_detected(detection.fireDetected)
            sprinkler.when_fire_detected(detection.fireDetected)
            notification.sendNotif("fire", "")

if __name__ == "__main__":
    main()