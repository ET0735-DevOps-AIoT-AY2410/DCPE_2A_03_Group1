import RPi.GPIO as GPIO
import time
from time import sleep
from hal import hal_lcd as LCD
import notification
from hal import hal_input_switch as switch
from threading import Thread

def init():
    GPIO.setmode(GPIO.BCM)
    switch.init()

def thread_isSwitchON(): # calls detached thread
    sos_thread = Thread(target=isSwitchON)
    sos_thread.start()

def isSwitchON():               # Check if SOS switch is ON
    while True:
        if switch.read_slide_switch() == 0: # switch ON
            print("SOS Switch Activated!")
            notification.sendNotif("help", "123 Main St, Singapore")            # Send notification to emergency services
            while (switch.read_slide_switch() == 0):
                time.sleep(0.1) # freeze code until switch OFF
        else: # switch OFF
            print("SOS Switch Deactivated.")
            while (switch.read_slide_switch() == 1):
                time.sleep(0.1) # freeze code until switch ON
    
# REQ-09	
# When the manual SOS switch (slide switch) is switched to ON for 3s, then update the bool helpNeeded to True. Which immediately alert for help

