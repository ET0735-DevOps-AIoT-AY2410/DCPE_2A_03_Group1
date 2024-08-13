import pytest
from unittest import mock
import src.sprinkler as sprinklertest
import RPIO.GPIO as GPIO

@mock.patch(sprinklertest.GPIO)

def test_gpio_setup(mock_gpio)
    sprinklertest.init()
    mock_gpio.setmode.assert_called_once_with(mock_gpio.BCM)
    mock_gpio.setwarnings.assert_called_once_with(False)
    mock_gpio.setup.assert_called_once_with(26, mock_gpio.OUT)

def test_set_servo_position():
    result = sprinklertest.set_servo_position()
    num = 1
    assert (result == num)

def test_when_fire_detected():
    result = sprinklertest.when_fire_detected()
    num = 0
    assert (result == num)

    