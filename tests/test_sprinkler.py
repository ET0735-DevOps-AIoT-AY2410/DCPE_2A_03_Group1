import pytest
from unittest import mock
from src import sprinkler as sprinklertest
import RPIO.GPIO as GPIO

@mock.patch(sprinklertest.GPIO)

def test_gpio_setup(mock_gpio):
    sprinklertest.init()
    mock_gpio.setmode.assert_called_once_with(mock_gpio.BCM)
    mock_gpio.setwarnings.assert_called_once_with(False)
    mock_gpio.setup.assert_called_once_with(26, mock_gpio.OUT)

def test_set_servo_position():              #Test if the servo position is set to 180 degrees
    sprinklertest.init()
    result = sprinklertest.set_servo_position(180)
    num = 2
    assert (result == num)

def test_when_fire_detected():          #Test if sprinkler turn on when fire is detected
    sprinklertest.init()
    result = sprinklertest.when_fire_detected(True)
    num = 2
    assert (result == num)

def test_calculate_servo_position():                    #Test the servo calculation function
    sprinklertest.init()
    result = sprinklertest.calculate_servo_position(180)   
    num = 2
    assert (result == num)   