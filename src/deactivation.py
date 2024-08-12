from hal import hal_rfid_reader as rfid 
from hal import hal_buzzer as buzzer
import notification as notif
import RPi.GPIO as GPIO
import alarm as turnoff
from threading import Thread
import time

fireDetected = False

def main():
    reader = rfid.init()
    buzzer.init()
    global fireDetected 
    rfid_scan(reader)

    rfid_thread = Thread(target=rfid_scan, args=(reader,))
    rfid_thread.start()
    fireDetected = True
    turnoff.when_fire_detected(fireDetected )


def rfid_scan(reader):  
    global fireDetected
    while True:
        if fireDetected:
            id = reader.read_id_no_block()
            id = str(id)
            print ("RFID id: " + id)
            fireDetected = False
            turnoff_alarm()
            notif.sendNotif("false_alarm", "Singapore Polytechnic")    
        time (0.5)

def turnoff_alarm():
    GPIO.output(24, 0)
    GPIO.output(18, 0)    
        
    

if __name__ == "__main__":
    main()
        






# REQ-10	
# In the case of a false alarm, when the RFID tag triggers the RFID sensor, it will update the bool fireDetected to False. Deactivating the fire alarm

