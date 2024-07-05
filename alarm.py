import time
from time import sleep
import RPi.GPIO as GPIO


#i assumed fire is detected (fireisdetected = true in main), so the fireIsDetected in main stays true to see if buzzer and led blinks as required.

def init():
    GPIO.setmode(GPIO.BCM)  
    GPIO.setwarnings(False)
    GPIO.setup(24, GPIO.OUT)  #gpio24 for led
    GPIO.setup(25, GPIO.OUT)  #gpio25 for buzzer

def when_fire_detected(fireDetected):
    while fireDetected == True:
        GPIO.output(24,1) #on
        GPIO.output(25,1)
        sleep(1)
        GPIO.output(24,0) #off
        GPIO.output(25,0)
        sleep(1)
        #i think shld be 0.5hz..? im not sure tho 

def main():
    init()
    fireIsDetected = True
    when_fire_detected(fireIsDetected)

if __name__ =="__main__":
    main()