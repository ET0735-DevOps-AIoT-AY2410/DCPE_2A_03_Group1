from hal import hal_temp_humidity_sensor as temp
from hal import hal_adc as adc
from hal import hal_lcd as LCD
from hal import hal_led as led
from hal import hal_ir_sensor as ir
import hmi as menu
import main as mainCode

import time
from threading import Thread
import queue

temperature_list = [30]     #initialize temperature list

def init():
    temp.init()
    adc.init()
    led.init()
    ir.init()
    lcd = LCD.lcd()
    lcd.lcd_clear()

def alarmStatus():                  #Check if fire detected
    temperature_list = pingtemp()
    adc_list = pingadc()
    average_temp = avgTemp(temperature_list)
    average_adc = avgADC(adc_list)

    
    if(average_temp > mainCode.tempThres or average_adc > mainCode.lightThres and pingSmoke()):
        return True
    return False
    


def pingtemp():    
    global temperature_list                          #Capture Temperature Values on last 5 seconds
    
    temp_reading = temp.read_temp_humidity()[0]
    if temp_reading>0:
        temperature = temp_reading
        temperature_list.append(temperature)
        if len(temperature_list) > 5:
            temperature_list.pop(0)              

    return temperature_list

def pingadc():                                  #Capture Light Values on last 5 seconds
    adc_list = []  
    
    adcvalue = adc.get_adc_value(0)
    time.sleep(0)
    adc_list.append(adcvalue/5)

    if len(adc_list) > 5:
        adc_list.pop(0) 

    return adc_list

def pingSmoke():                              #Check if Smoke Detected
    smokeDetected = ir.get_ir_sensor_state()
    if smokeDetected:
        return True
    return False

def avgADC(adc_list):                      #Calculate Average Light Intensity
    average_adc = 0
    if len(adc_list) > 0:
        average_adc = sum(adc_list) / len(adc_list)
    else:
        average_adc = 0
    return average_adc

def avgTemp(temperature_list):                                      #Calculate Average Temperature
    average_temp = 0
    if len(temperature_list) > 0:                                          
        average_temp = sum(temperature_list) / len(temperature_list)
    else:
        average_temp = 0
    return average_temp

def listUpdate(list):                          #Update List
    if len(list) > 5:  
        list.pop(0)

def main():
    init()

if __name__ == "__main__":
    main()


