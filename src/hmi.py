import time
from threading import Thread
import queue
from hal import hal_lcd as LCD
import keypad
import detection
import main as mainCode

def init():
    #initialization of HAL modules
    global lcd
    lcd = LCD.lcd()
    lcd.lcd_clear()

def main():
    init()

def scannerMode():
    lcd.lcd_display_string("Scanning Now", 1)
    displayTemp = detection.pingtemp()[-1]
    displayAdc = detection.pingadc()[-1]
    lcd.lcd_display_string(f"T:{displayTemp} L:{displayAdc}",2)

def adjustMode():
    lcd = LCD.lcd()
    lcd.lcd_clear()
    lcd.lcd_display_string("Welcome to", 1)
    lcd.lcd_display_string("Adjustment Mode", 2)
    time.sleep(2)
    lcd.lcd_clear()

    while True:
        lcd.lcd_display_string(f"1-TempThres:{mainCode.tempThres}", 1)
        lcd.lcd_display_string(f"2-LghtThres:{mainCode.lightThres}", 2)

        key = keypad.shared_keypad_queue.get()

        if(key == 1): # if keypad = 1, change temp threshold
            newTempThres = ""
            while(True):
                lcd.lcd_clear()
                lcd.lcd_display_string("Temp Thresholds", 1)
                lcd.lcd_display_string(f"Old:{mainCode.tempThres}, New:{newTempThres}", 2)
                
                input = keypad.shared_keypad_queue.get()
                if input: # any key pressed
                    if input == '*': # save & exit
                        mainCode.tempThres = int(newTempThres)
                        break
                    elif input == '#': # backspace
                        newTempThres = newTempThres[:-1] # removes last character
                    else: # input 0-9
                        newTempThres += str(input)
            lcd.lcd_clear()

        elif(key == 2): #if keypad = 2, change light threshold
            newLightThres = ""
            while(True):
                lcd.lcd_clear()
                lcd.lcd_display_string("Light Thresholds", 1)
                lcd.lcd_display_string(f"Old:{mainCode.lightThres}, New:{newLightThres}", 2)

                input = keypad.shared_keypad_queue.get()
                if input: # any key pressed
                    if input == '*': # save & exit
                        mainCode.lightThres = int(newLightThres)
                        break
                    elif input == '#': # backspace
                        newLightThres = newLightThres[:-1] # removes last character
                    else: # input 0-9
                        newLightThres += str(input)
            lcd.lcd_clear()
            
        elif(key == '*'):
            break
    lcd.lcd_clear()
    

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