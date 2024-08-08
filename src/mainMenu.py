
# REQ-01
# When the System turns on, the following active detection menu will be displayed. Format temperature and light intensity to 2 SF. Constantly update the LCD to display the latest temperature and light intensity values. When scanning, LCD will display:
#
#	 Line 1 = “Scanning Now.”
#	 Line 2 = “Temp:xx Light:xx” 

# REQ-02
# While in the main menu defined in REQ-01, if key # is entered in the keypad, enter the sensitivity adjustment menu below:
#
# If key * is entered in the keypad, terminate the sensitivity adjustment and return to main menu
# 
# xx represents the old temperature threshold and yy should constantly update to display the currently read temperature value from sensor. Display the following lines in LCD and store collected data: 
# 
# 	 Line 1 = “Old Temp: xx”
#  	 Line 2 = “New thrshld: yy”

# REQ-03	
# While in the adjustment menu defined in REQ-02, if key # is entered in the keypad, enter the sensitivity adjustment menu below:
# 
# If key # is entered in the keypad, terminate the sensitivity adjustment and return to main menu 
# 
# xx represents the old light threshold and yy should constantly update to display the currently read light value from sensor. Display the following lines in LCD and store collected data:
# 
# 	 Line 1 = “Old Light: xx”
# 	 Line 2 = “New thrshld: yy”
# After entering # in the keypad, return to main menu in REQ-01.


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

    start(lcd)
    


def start(lcd):
    oldTemperature = 0
    temperature = 0

    light = 0
    oldLight = 0

    scanner = True
    adjustment = False
    display = False

    temp_list = detection.pingtemp()
    adc_list = detection.pingadc()
    detection.listUpdate()

    while True:
        while(scanner):
            lcd.lcd_display_string("Sensors Scanning", 1)                                                      #Display Scanning & Temp/Light values
            lcd.lcd_display_string("T:" + temp_list[4] + "L:" + adc_list[4] ,2)

            temp_list = detection.pingtemp()
            adc_list = detection.pingadc()

            keyvalue = shared_keypad_queue.get()

            if(keyvalue == 0):                         #if keypad '0' pressed, switch to adjustment system             
                scanner = False
                adjustment = True

        while(adjustment):
            lcd.lcd_clear()
            lcd.lcd_display_string("Temp Thres:'1'", 1)
            lcd.lcd_display_string("Light Thres:'2'", 2)

            key = shared_keypad_queue.get()

            if(key == 1):                                             #if keypad = 1, change temp threshold
                lcd.lcd_clear()
                lcd.lcd_display_string("Enter Temp Thres", 1)
                oldTemperature = temperature

                temperature = int(input_from_keypad())

                lcd.lcd_clear()
                while(True):
                    lcd.lcd_display_string("Old Temp:" + str(oldTemperature),1)
                    lcd.lcd_display_string("New Temp:" + str(temperature),2)
                    if shared_keypad_queue.get() == '*':
                        break
            
            elif(key == 2):                                                   #if keypad = 2, change light threshold
                lcd.lcd_clear()
                lcd.lcd_display_string("Enter ADC Thres", 1)
                oldLight = light 

                light = int(input_from_keypad())

                lcd.lcd_clear()
                while(True):
                    lcd.lcd_display_string("Old Light:" + str(oldLight),1)
                    lcd.lcd_display_string("New Light:" + str(light),2)
                    if shared_keypad_queue.get() == '*':
                        break

            
            #Exit adjustment mode and return to scanner mode
            adjustment = False
            scanner = True
    
def input_from_keypad():
    value = ""
    while (True):
        key = shared_keypad_queue.get()
        if key == '#':                  #key # to break away from entering value
            break
        value += str(key)
    return value


if __name__ == "__main__":
    main()



