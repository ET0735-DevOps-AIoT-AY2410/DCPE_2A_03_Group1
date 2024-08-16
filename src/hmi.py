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
            lcd.lcd_clear()
            newTempThres = ""
            while(True):
                lcd.lcd_display_string("Temp Thresholds", 1)
                lcd.lcd_display_string(f"Old:{mainCode.tempThres}, New:{newTempThres}", 2)
                
                input = keypad.shared_keypad_queue.get()
                if input: # any key pressed
                    if input == '*': # save & exit
                        mainCode.tempThres = int(newTempThres)
                        break
                    elif input == '#': # backspace
                        newTempThres = newTempThres[:-1] # removes last character
                        lcd.lcd_clear()
                        lcd.lcd_display_string(f"Old:{mainCode.tempThres}, New:{newTempThres}", 2)
                    else: # input 0-9
                        newTempThres += str(input)
            lcd.lcd_clear()

        elif(key == 2): #if keypad = 2, change light threshold
            lcd.lcd_clear()
            newLightThres = ""
            while(True):
                lcd.lcd_display_string("Light Thresholds", 1)
                lcd.lcd_display_string(f"Old:{mainCode.lightThres}, New:{newLightThres}", 2)

                input = keypad.shared_keypad_queue.get()
                if input: # any key pressed
                    if input == '*': # save & exit
                        mainCode.lightThres = int(newLightThres)
                        break
                    elif input == '#': # backspace
                        newLightThres = newLightThres[:-1] # removes last character
                        lcd.lcd_clear()
                        lcd.lcd_display_string(f"Old:{mainCode.lightThres}, New:{newLightThres}", 2)
                    else: # input 0-9
                        newLightThres += str(input)
            lcd.lcd_clear()
            
        elif(key == '*'):
            break
    lcd.lcd_clear()
    

if __name__ == "__main__":
    main()