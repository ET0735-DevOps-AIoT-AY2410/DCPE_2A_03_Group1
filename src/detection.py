from hal import hal_temp_humidity_sensor as temp
from hal import hal_adc as adc
from hal import hal_lcd as LCD
from hal import hal_led as led

import time
from threading import Thread
import queue

temperature_list = []
adc_list = []    
average_temp = 0


def main():
    temp.init()
    adc.init()

    #initialization of HAL modules
    led.init()
 
    lcd = LCD.lcd()
    lcd.lcd_clear()

    alarm = False

    while (True):

        pingtemp()      #run temp
        pingadc()       #run adc

        avgTemp()

        alarmStatus()

        listUpdate()
        
        lcd.lcd_display_string ("Last 5 temperature" + temperature_list[4], 1)
        lcd.lcd_display_string ("Last 5 light intensity" + adc_list[4], 2)

def pingtemp():                                 #Capture Temperature Values on last 5 seconds
    temperature = temp.read_temp_humidity()    
    time.sleep(1)            
    temperature_list.append(temperature)

def pingadc():                                  #Capture ADC Values on last 5 seconds
    adcvalue = adc.get_adc_value()
    time.sleep(1)
    adc_list.append(adcvalue)

def avgTemp():
    if len(temperature_list) > 0:                                           #Calculate Average Temperature
        average_temp = sum(temperature_list) / len(temperature_list)
    else:
        average_temp = 0

def alarmStatus():
    if (temperature_list[4] > (average_temp + 5)):
        alarm = True
    else:
        alarm = False

def listUpdate():
    if len(temperature_list) > 5:  
        temperature_list.pop(0)

    if len(adc_list) > 5:
        adc_list.pop(0)





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



