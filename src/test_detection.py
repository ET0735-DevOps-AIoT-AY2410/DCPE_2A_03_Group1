import detection
import time

def test_pingtemp_positive():               #Test if temperature values are positive  
    for i in range(5):
        temp_list = detection.temperature_list      #Run functions 5 time to simulate sequence of readings
        time.sleep(0.5)
    
    assert all(temp > 0 for temp in temp_list)
    
def test_pingtemp():
    for i in range(5):
        temp_list = detection.pingtemp()        #Run functions 5 time to simulate sequence of readings
        time.sleep(0.5)
    
    assert len(temp_list) == 5           #Check if list has 5 values

def test_pingadc():
    for i in range(5):
        adc_list = detection.pingadc()          #Run functions 5 time to simulate sequence of readings
        time.sleep(0.5)
    
    assert len(adc_list) == 5           #Check if list has 5 values

def test_pingSmoke():
    smoke_Detected = detection.pingSmoke()      #Check if smoke is detected
    
    assert isinstance(smoke_Detected, bool)     #Check if return value is boolean

def test_avgADC():
    adc_list = detection.pingadc()          #Get real data
    average_adc = detection.avgADC(adc_list)        #Calculate average

    assert 0 <= average_adc <= 1023          #Check if average is within ADC range

def test_avgTemp():
    temp_list = detection.pingtemp()        #Get real data
    average_temp = detection.avgTemp(temp_list)      #Calculate average

    assert 0 <= average_temp <= 100          #Check if average is within temperature range