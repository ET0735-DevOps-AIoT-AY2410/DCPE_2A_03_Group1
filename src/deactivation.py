from hal import hal_rfid_reader as rfid 
from hal import hal_buzzer as buzzer
import notification as notif
<<<<<<< HEAD
=======
import RPi.GPIO as GPIO
>>>>>>> df472c47e94deaf666f424d493e5d357f356fb61
import alarm as turnoff

def main():
    reader = rfid.init()
    buzzer.init()
    fireDetected = True
    false_alarm(reader)

def false_alarm(reader):
    id = reader.read_id_no_block()
    id = str(id)

    if id != "NONE":
<<<<<<< HEAD
        fireDetected = True
        turnoff.when_fire_detected(fireDetected)
        print ("false alarm")
        print (id)
        notif.sendNotif(false_alarm, "271, boon lay drive")    
=======
        turnoff.when_fire_detected(False)
        print ("false alarm")
        fireDetected = False
        print (id)
        notif.sendNotif(false_alarm, "")    
>>>>>>> df472c47e94deaf666f424d493e5d357f356fb61
    return fireDetected
    

if __name__ == "__main__":
    main()



# REQ-10	
# In the case of a false alarm, when the RFID tag triggers the RFID sensor, it will update the bool fireDetected to False. Deactivating the fire alarm

