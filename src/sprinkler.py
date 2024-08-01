import time
from time import sleep
import RPi.GPIO as GPIO

def init():
    GPIO.setmode(GPIO.BCM)  # choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(26, GPIO.OUT)  # set GPIO 26 as output

def set_servo_position(position):
    PWM = GPIO.PWM(26,50)
    position = (-10*position)/180 + 12
    PWM.start(position)
    sleep(0.1)
    PWM.stop()

def when_fire_detected(fire_detected):

    if fire_detected == True:
        set_servo_position(180)
    else:    
        set_servo_position(0)


def main():
    init()
    set_servo_position(0)
    fireIsDetected = True
    when_fire_detected(fireIsDetected)
    sleep(6)
    fireIsDetected = False
    when_fire_detected(fireIsDetected)


if __name__ =="__main__":
    main() 