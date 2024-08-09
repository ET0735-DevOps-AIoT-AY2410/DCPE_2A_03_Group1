
# REQ-13	
# When the fire is detected (fireDetected = True) OR manual SOS switch is activated (helpNeeded = True), send an automated Telegram alert to SCDF.

# REQ-14	
# The notification must specify if the situation is a fire or elderly needing urgent help.

# REQ-15	
# The notification system must include the location of the fire/activated switch within the house to assist first responders

import requests 

def debug(): # for testing notifications ONLY
    selectionInput = input('1: Fire\n2: Help needed\n3: False Alarm\nWhat is the situation? ')
    locationInput = input('What is the location? ')
    if (int(selectionInput) == 1): 
        sendNotif("fire", locationInput)
    elif (int(selectionInput) == 2):
        sendNotif("help", locationInput)
    elif (int(selectionInput) == 3):
        sendNotif("help", locationInput)
    else:
        print("ERROR: Invalid Selection")

# To send a notification, use sendNotif(type, location)
    # type must be "fire" or "help" or "false_alarm"
    # location must be a string
    
def sendNotif(type, location): # call this function from other codes
    token = "7317584084:AAFmG-5ZwZwNfU8fAiypMp56qsEmmEDKy00"
    chatID = "5896827510"
    msgHeader_dict = {
        "fire" : "FIRE DETECTED. Fire Alarm has been Activated",
        "help" : "URGENT HELP NEEDED. SOS Switch has been Activated",
        "false_alarm" : "FALSE ALARM. Fire Alarm has been Deactivated"
    }
    message = f"{msgHeader_dict[type]}\nLocation: {location}"
    url_sendMessage = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatID}&text={message}"
    print(requests.get(url_sendMessage).json()) # sends msg
    print("Notification of type: " + str(type) + " sent to SCDF_Bot")

if __name__ == "__main__":
    while(True):
        debug()    