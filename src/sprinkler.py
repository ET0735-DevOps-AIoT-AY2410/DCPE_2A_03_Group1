import time
from time import sleep
import RPi.GPIO as GPIO
import main as mainCode
from threading import Thread



global RetForTest
def init():
    GPIO.setmode(GPIO.BCM)  # choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(26, GPIO.OUT)  # set GPIO 26 as output

def set_servo_position(position):
    PWM = GPIO.PWM(26,50)
    cycle = calculate_servo_position(position)
    PWM.start(cycle)
    sleep(0.1)
    PWM.stop()
    return cycle

def when_fire_detected(fireDetection):
    if fireDetection == True:
        set_servo_position(180)
    else:
        set_servo_position(0)

def calculate_servo_position(position):
    return (-10 * position) / 180 + 12

def thread_when_fire_detected():
    alarm_thread=Thread(target=when_fire_detected)
    alarm_thread.start()

def main():
    init()

if __name__ =="__main__":
    main() 