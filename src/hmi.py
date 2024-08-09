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
    print("keyyypreseed")
    shared_keypad_queue.put(key)

def init():
    global shared_keypad_queue
    #initialization of HAL modules
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    lcdStart()

def main():
    lcdStart()

def lcdStart():
    lcd = LCD.lcd()
    lcd.lcd_clear()

def scannerMode():
    lcd = LCD.lcd()
    lcd.lcd_clear()
    lcd.lcd_display_string("Scanning Now", 1)
    time.sleep(3)
    
    while True: # CHANGE THIS TO NOT LOOP FOREVER
        displayTemp = detection.pingtemp()[-1]
        displayAdc = detection.pingadc()[-1]

        lcd.lcd_display_string(f"T:{displayTemp} L:{displayAdc}",2)                #Display Scanning & Temp/Light values
        time.sleep(1)

def adjustMode():
    lcd = LCD.lcd()
    global newTempThres # global - so all functions can use this
    global newLightThres 
    global oldLightThres
    global oldTempThres 
    oldTempThres = 0
    newTempThres = 0
    oldLightThres = 0
    newLightThres = 0
    lcd.lcd_clear()
    lcd.lcd_display_string("Welcome to", 1)
    lcd.lcd_display_string("Adjustment Mode", 2)
    time.sleep(3)

    lcd.lcd_clear()
    lcd.lcd_display_string("Temp Thres:'1'", 1)
    lcd.lcd_display_string("Light Thres:'2'", 2)

    key = shared_keypad_queue.get()

    if(key == 1):                                          #if keypad = 1, change temp threshold
        lcd.lcd_clear()
        lcd.lcd_display_string("Enter Temp Thres", 1)
        oldTempThres = newTempThres
        newTempThres = int(input_from_keypad())
        print("hi3")
        print("newTempThres", newTempThres)

        lcd.lcd_clear()
        while(True):
            lcd.lcd_display_string("Temp Thresholds", 1)
            lcd.lcd_display_string("Old:" + str(oldTempThres) + ", New:" + str(newTempThres),2)
            if shared_keypad_queue.get() == '*':
                break
            
    elif(key == 2):                                                   #if keypad = 2, change light threshold
        lcd.lcd_clear()
        lcd.lcd_display_string("Enter ADC Thres", 1)
        oldLightThres = newLightThres 

        newLightThres = int(input_from_keypad())
        print("newLightThres", newLightThres)

        lcd.lcd_clear()
        while(True):
            lcd.lcd_display_string("Light Thresholds", 1)
            lcd.lcd_display_string("Old:" + str(oldLightThres) + ", New:" + str(newLightThres),2)
            if shared_keypad_queue.get() == '*':
                break

def thread_scannerMode():
    scanner_thread = Thread(target=scannerMode)
    scanner_thread.start()

def thread_adjustMode():
    adjust_thread = Thread(target=adjustMode)
    adjust_thread.start()

def input_from_keypad():
    value = ""
    while (True):
        key = shared_keypad_queue.get()
        if key == '#':                  #key # to break away from entering value
            break
        value += str(key)

        print("key inputted:" + str(key))
        print("full list: " + str(value))
    return value

if __name__ == "__main__":
    main()



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