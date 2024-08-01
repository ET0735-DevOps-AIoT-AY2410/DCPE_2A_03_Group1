from hal import hal_rfid_reader as rfid 
from hal import hal_buzzer as buzzer
import RPi.GPIO as GPIO

def main():
    reader = rfid.init()
    buzzer.init()
    fireDetected = True

    def false_alarm():
        id = reader.read_id_no_block()
        id = str(id)

        if id != "NONE":
            GPIO.output(24,0) 
            print ("false alarm")
            fireDetected = False
            print (id)
        
        return fireDetected
    

if __name__ == "__main__":
    main()
        






# REQ-10	
# In the case of a false alarm, when the RFID tag triggers the RFID sensor, it will update the bool fireDetected to False. Deactivating the fire alarm

