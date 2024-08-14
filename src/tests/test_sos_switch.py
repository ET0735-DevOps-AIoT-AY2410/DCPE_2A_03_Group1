import pytest
import time
import RPI.GPIO as GPIO
from src import sos_switch as sos

def test_init():
    sos.init()
    assert GPIO.getmode() == GPIO.BCM

def test_switch_read_slide_switch_off(): 
    sos.init()       
    assert sos.switch.read_slide_switch() == 1       #test that the switch is off
    
def test_switch_read_slide_switch_on():
    sos.init()
    assert sos.switch.read_slide_switch() == 0       #test that the switch is on