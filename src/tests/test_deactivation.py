from .. import deactivation as deacttest
import pytest
from unittest import mock
#import RPI.GPIO as GPIO

@mock.patch(deacttest.rfid_scan)
@mock.patch(deacttest.turnoff_alarm)
@mock.patch(deacttest.turnOff_sprinkler)

def test_rfid_scan(mock_rfid_init, mock_sendNotif, mock_turnoff_alarm, mock_turnOff_sprinkler):
    # Mock the RFID reader
    mock_reader = mock.Mock()
    mock_reader.read_id_no_block.return_value = "834711133486"
    mock_rfid_init.return_value = mock_reader

    # Run the function with fireDetected set to True
    result = deacttest.rfid_scan(True)

    # Assert that the notification was sent
    mock_sendNotif.assert_called_once_with("false_alarm", "123456 Dover Road #01-01")

    # Assert that the alarm and sprinkler were turned off
    mock_turnoff_alarm.assert_called_once()
    mock_turnOff_sprinkler.assert_called_once()

    # Assert that the function returned 3
    assert result == 3