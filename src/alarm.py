
# REQ-11	
# When the fire is detected (fireDetected = True), buzzer will constantly play a loud sound ON and OFF at 0.5Hz until fire alarm is turned off.

# REQ-12	
# When the fire is detected (fireDetected = True), LED must blink OFF and ON  at 0.5Hz constantly until fire alarm is turned off.

import time
from time import sleep
import RPi.GPIO as GPIO
from threading import Thread


#i assumed fire is detected (fireisdetected = true in main), so the fireIsDetected in main stays true to see if buzzer and led blinks as required.

def init():
    GPIO.setmode(GPIO.BCM)  
    GPIO.setwarnings(False)
    GPIO.setup(24, GPIO.OUT)  #gpio24 for led
    GPIO.setup(18, GPIO.OUT)  #gpio25 for buzzer

def when_fire_detected(fireDetected):
    while fireDetected == True:
        GPIO.output(24,1) #on
        GPIO.output(18,1)
        sleep(1)
        GPIO.output(24,0) #off
        GPIO.output(18,0)
        sleep(1)


def alarmThread(fireIsDetected):
alarm_thread=Thread(target= when_fire_detected, args= (fireIsDetected, ))
alarm_thread.start()

def main():
    init()
    fireIsDetected = True
    when_fire_detected(fireIsDetected)

if __name__ =="__main__":
    main() 