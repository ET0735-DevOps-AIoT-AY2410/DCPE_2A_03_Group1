#import RPI.GPIO as GPIO
from unittest import mock
import src.alarm as alarmtest
import pytest

@mock.patch(alarmtest)

def test_setup_gpio(mock_gpio):
    alarmtest.init()
    mock_gpio.setmode.assert_called_once_with(mock_gpio.BCM)
    mock_gpio.setup.assert_any_call(18, mock_gpio.OUT)
    mock_gpio.setup.assert_any_call(24, mock_gpio.OUT)
    assert 0

def test_when_fire_detected(mock_gpio):
    alarmtest.when_fire_detected()
    mock_gpio.output.assert_called_once_with(18, 1)
    mock_gpio.output.assert_called_once_with(18, 0)
    assert 1



    