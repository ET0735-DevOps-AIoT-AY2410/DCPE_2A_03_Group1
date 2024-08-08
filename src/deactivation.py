from hal import hal_rfid_reader as rfid 
from hal import hal_buzzer as buzzer
import notification as notif
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
        fireDetected = True
        turnoff.when_fire_detected(fireDetected)
        print ("false alarm")
        print (id)
        notif.sendNotif(false_alarm, "271, boon lay drive")    
    return fireDetected
    

if __name__ == "__main__":
    main()



# REQ-10	
# In the case of a false alarm, when the RFID tag triggers the RFID sensor, it will update the bool fireDetected to False. Deactivating the fire alarm

