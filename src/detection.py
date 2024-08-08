from hal import hal_temp_humidity_sensor as temp
from hal import hal_adc as adc
from hal import hal_lcd as LCD
from hal import hal_led as led
import hmi as menu

import time
from threading import Thread
import queue

def init():
    temp.init()
    adc.init()
    led.init()
    lcd = LCD.lcd()
    lcd.lcd_clear()


def alarmStatus():
    fireDetected = False

    tempThres = menu.ReturnTempThres
    lightThres = menu.ReturnADCThres

    temperature_list = pingtemp()
    adc_list = pingadc()

    average_temp = avgTemp(temperature_list)
    average_adc = avgADC(adc_list)
    
    if(average_temp > tempThres or average_adc> lightThres):
        fireDetected = True
    else:
        fireDetected = False

    return fireDetected

def pingtemp():    
    temperature_list = []                           #Capture Temperature Values on last 5 seconds
    
    temperature = temp.read_temp_humidity()[0]             
    temperature_list.append(temperature)

    if len(temperature_list) > 5:
        temperature_list.pop(0) 

    return temperature_list

def pingadc():                                  #Capture ADC Values on last 5 seconds
    adc_list = []  
    
    adcvalue = adc.get_adc_value(0)
    adc_list.append(adcvalue)

    if len(adc_list) > 5:
        adc_list.pop(0) 

    return adc_list

def avgADC(adc_list):
    average_adc = 0
    if len(adc_list) > 0:
        average_adc = sum(adc_list) / len(adc_list)
    else:
        average_adc = 0
    return average_adc

def avgTemp(temperature_list):
    average_temp = 0
    if len(temperature_list) > 0:                                           #Calculate Average Temperature
        average_temp = sum(temperature_list) / len(temperature_list)
    else:
        average_temp = 0
    return average_temp

def listUpdate(list):
    if len(list) > 5:  
        list.pop(0)



def main():
    init()
    while (True):
        pingtemp()      #run temp
        pingadc()       #run adc
        average_temp = avgTemp()
        
        print("avg temperature:" + str(average_temp))
        print("Last 5 temperatures: " + str(temperature_list))
        print("Last 5 light intensity: " + str(adc_list))

if __name__ == "__main__":
    main()

# REQ-04	
# Constantly ping sensors to collect data on the temperature and light intensity in the surroundings. Store the last 5 recorded data (of temperature and light intensity) in an array. 

# REQ-05	
# Take and store the mean value of the last 5 recorded data in REQ-04. This mean value will be used to compare with threshold values to detect abnormally high temperature/light intensity.

# REQ-06
# Every 10s:
# IF mean detected temperature > fire detection threshold temperature
# OR mean detected light intensity > fire detection threshold light intensity,
# update the bool fireDetected to True. LCD will override main menu and display:
#   Line 1 = “Fire Detected”
#   Line 2 = “Alerted SCDF”

# REQ-07
# Locate and store data on the location of the sensor that sensed the fire.

# REQ-08	
# Otherwise, if the fire detection conditions in REQ-06 are false,
# LCD will momentarily override main menu and display:
#	Line 1 = “No Fire Detected”
#	Line 2 = “Temp:xx Light:xx”



