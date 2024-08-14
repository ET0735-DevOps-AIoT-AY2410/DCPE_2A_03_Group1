from hal import hal_rfid_reader as rfid 
from hal import hal_buzzer as buzzer
import notification as notif
import RPi.GPIO as GPIO
import alarm as alarm
from threading import Thread
import time
import alarm
import main as mainCode
import sprinkler

def init():
    GPIO.setmode(GPIO.BCM)  
    GPIO.setwarnings(False)
    GPIO.setup(24, GPIO.OUT)  #gpio24 for led
    GPIO.setup(18, GPIO.OUT)  #gpio25 for buzzer

def rfid_scan(fireDetected):
    global rfid_thread
    global stopThread
    global breakLoop
    stopThread = False
    reader = rfid.init()
    while True:
        if fireDetected:
            id = reader.read_id_no_block()
            id = str(id)
            print ("RFID id: " + id)
            if (id == "834711133486"): 
                notif.sendNotif("false_alarm", "123456 Dover Road #01-01") 
                alarm.stopThread = True
                mainCode.fireDetection = False
                return 3
        time.sleep(0.5)

def rfidThread(fireDetected):
    global rfid_thread
    rfid_thread = Thread(target=rfid_scan, args=(fireDetected,))
    rfid_thread.start()