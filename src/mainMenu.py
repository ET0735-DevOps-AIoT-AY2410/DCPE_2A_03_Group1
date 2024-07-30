import time
from threading import Thread
import queue

from hal import hal_lcd as LCD
from hal import hal_keypad as keypad


import detection

#Empty list to store sequence of keypad presses
shared_keypad_queue = queue.Queue()



#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    shared_keypad_queue.put(key)


def main():
    #initialization of HAL modules

    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

    lcd = LCD.lcd()
    lcd.lcd_clear()

    start()
    


def start():
    oldTemperature = 0
    temperature = 0

    light = 0
    oldLight = 0

    scanner = True
    adjustment = False
    LCD.lcd.lcd_display_string

    while(scanner):
        LCD.lcd.lcd_display_string("Sensors Scanning", 1)                                                      #Display Scanning & Temp/Light values
        LCD.lcd.lcd_display_string("Temp: 1" + "Light: 2" ,2)

        keyvalue= shared_keypad_queue.get()

        if(keyvalue == 0):                         #if keypad '0' pressed, switch to adjustment system             
            scanner = False
            adjustment = True
            
        else:
            scanner = True

    while(adjustment):
        LCD.lcd.lcd_clear
        LCD.lcd.lcd_display_string("Temp Thres:'1'", 1)
        LCD.lcd.lcd_display_string("Light Thres:'2'", 2)

        key = shared_keypad_queue.get()

        if(key == '1'):                                             #if keypad = 1, change temp threshold
            LCD.lcd.lcd_clear
            LCD.lcd.lcd_display_string("Enter Temp Thres", 1)
            oldTemperature = temperature

            temperature = int(input_from_keypad())

            LCD.lcd.lcd_clear
            LCD.lcd.lcd_display_string("Old Temp:" + str(oldTemperature),1)
            LCD.lcd.lcd_display_string("New Temp:" + str(temperature),2)
        elif(key == '2'):                                                   #if keypad = 2, change light threshold
            LCD.lcd.lcd_clear
            LCD.lcd.lcd_display_string("Enter ADC Thres", 1)
            oldLight = light 

            light = int(input_from_keypad)

            LCD.lcd.lcd_clear
            LCD.lcd.lcd_display_string("Old Light:" + str(oldLight),1)
            LCD.lcd.lcd_display_string("New Light:" + str(light),2)

    
def input_from_keypad():
    value = ""
    while (True):
        key = shared_keypad_queue.get()
        if key == '#':                  #key # to break away from entering value
            break
        value = str(key)
    return value

        

if __name__ == "__main__":
    main()