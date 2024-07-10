import time
from threading import Thread
import queue

from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_adc as adc
from hal import hal_buzzer as buzzer
from hal import hal_keypad as keypad
from hal import hal_moisture_sensor as moisture_sensor
from hal import hal_input_switch as input_switch
from hal import hal_ir_sensor as ir_sensor
from hal import hal_rfid_reader as rfid_reader
from hal import hal_servo as servo
from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_usonic as usonic
from hal import hal_dc_motor as dc_motor
from hal import hal_accelerometer as accel

import detection

#Empty list to store sequence of keypad presses
shared_keypad_queue = queue.Queue()

IsKeyPressed = False


#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    shared_keypad_queue.put(key)
    IsKeyPressed = True


def main():
    #initialization of HAL modules
    led.init()
    adc.init()
    buzzer.init()
  
    moisture_sensor.init()
    input_switch.init()
    ir_sensor.init()
    reader = rfid_reader.init()
    servo.init()
    temp_humid_sensor.init()
    usonic.init()
    dc_motor.init()
    accelerometer = accel.init()

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

    systemON = True
    adjustment = False
    LCD.lcd.lcd_display_string

    while(systemON):
        LCD.lcd.lcd_display_string("Sensors Scanning", 1)
        LCD.lcd.lcd_display_string("Temp:" + detection.temp + "Light:" + detection.light,2)

        keyvalue= shared_keypad_queue.get()

        if(keyvalue == 0):
            systemON = False
            adjustment = True
            
        else:
            systemON = True

    while(adjustment):
        LCD.lcd.lcd_clear
        LCD.lcd.lcd_display_string("Temp Thres:'*'")
        LCD.lcd.lcd_display_string("Light Thres:'#'")

        key = shared_keypad_queue.get()

        if(key == '*'):
            LCD.lcd.lcd_clear

            LCD.lcd.lcd_display_string("Enter New Temperature Threshold")
            oldTemperature = temperature
            temperature = shared_keypad_queue.get()

            LCD.lcd.lcd_clear
        
            LCD.lcd.lcd_display_string("Old Temperature:" + oldTemperature,1)
            LCD.lcd.lcd_display_string("New Temperature:" + temperature,2)
        elif(key == '#'):
            LCD.lcd.lcd_clear

            LCD.lcd.lcd_display_string("Enter Light Threshold")
            oldLight = light 
            light = shared_keypad_queue.get()

            LCD.lcd.lcd_clear

            LCD.lcd.lcd_display_string("Old Light:" + oldLight,1)
            LCD.lcd.lcd_display_string("New Light:" + light,2)

    


        
