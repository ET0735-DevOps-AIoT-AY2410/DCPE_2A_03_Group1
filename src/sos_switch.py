import RPi.GPIO as GPIO
import time
from time import sleep
from hal import hal_lcd as LCD
import notification
from hal import hal_input_switch as switch
from threading import Thread

helpNeeded = False

def init():
    GPIO.setmode(GPIO.BCM)
    switch.init()

def isSwitchON():
    while True:
        if switch.read_slide_switch() == 0:
            helpNeeded = True
            print("Help Needed!")
            #LCD.lcd.lcd_clear
            #LCD.lcd().lcd_display_string("Help Needed!",1)
            notification.sendNotif("help", "switch")    #Alert
            time.sleep(3)
        else:
            print("No help needed")
            time.sleep(5)

def threadStartSOS():
    sos_thread = Thread(target=isSwitchON)
    sos_thread.start()


def main():
    init()
    
                    
if __name__ == "__main__":
    main()
    


# REQ-09	
# When the manual SOS switch (slide switch) is switched to ON for 3s, then update the bool helpNeeded to True. Which immediately alert for help

