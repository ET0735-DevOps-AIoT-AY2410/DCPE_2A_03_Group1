
# REQ-13	
# When the fire is detected (fireDetected = True) OR manual SOS switch is activated (helpNeeded = True), send an automated Telegram alert to SCDF.

# REQ-14	
# The notification must specify if the situation is a fire or elderly needing urgent help.

# REQ-15	
# The notification system must include the location of the fire/activated switch within the house to assist first responders

# To send a notification, use sendNotif(type, location)
    # type must be "fire" or "help"
    # location must be a string

import requests 

token = "6745515213:AAFjfoODFwsKv7FUzzdTig-cf-VNDILn80U"
chatID = "5896827510"

def main():
    selectionInput = input('1: Fire\n2: Help needed\nWhat is the situation? ')
    locationInput = input('What is the location? ')
    if (int(selectionInput) == 1): 
        sendNotif("fire", locationInput)
    elif (int(selectionInput) == 2):
        sendNotif("help", locationInput)
    else:
        print("ERROR: Invalid Selection")

def sendNotif(type, location):
    msgHeader_dict = {
        "fire" : "FIRE ALARM ACTIVATED",
        "help" : "URGENT HELP NEEDED",
        "false_alarm" : "FALSE ALARM. FIRE ALARM DEACTIVATED"
    }
    message = f"{msgHeader_dict[type]}\nLocation: {location}"
    url_sendMessage = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatID}&text={message}"
    print(requests.get(url_sendMessage).json()) # sends msg
    print("Message Sent")

if __name__ == "__main__":
    while(True):
        main()    