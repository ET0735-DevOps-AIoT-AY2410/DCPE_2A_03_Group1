import RPi.GPIO as GPIO
import time
from time import sleep
from hal import hal_lcd as LCD
import notification

helpNeeded = False

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #setup for switch

def switchON():
    while True:
        start_time = None
        if GPIO.input(17) == GPIO.LOW:
            start_time = time.time() #initialize starting time

            while GPIO.input(17) == GPIO.LOW:
                if time.time() - start_time >= 3:
                    helpNeeded = True
                    print("Help Needed!")
                    LCD.lcd().lcd_clear
                    LCD.lcd().lcd_display_string("Help Needed!",1)
                    notification.sendNotif("help", "")    #Alert
                    break

def main():
    init()
    switchON()
    
                    
if __name__ == "__main__":
    main()
    


# REQ-09	
# When the manual SOS switch (slide switch) is switched to ON for 3s, then update the bool helpNeeded to True. Which immediately alert for help

