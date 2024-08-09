import main as mainCode
import RPi.GPIO as GPIO
from hal import hal_input_switch as switch

# this code will test if the deatched thread can detect
# the change in fireDetection and update accordingly

def main():
    mainCode.init()
    mainCode.init_threads()
    while True:
        #print(str(alarm.fireIsDetected))
        if switch.read_slide_switch() == 0: # switch ON
            mainCode.fireDetection = True
        else: # switch OFF
            mainCode.fireDetection = False

if __name__ == "__main__":
    main()

