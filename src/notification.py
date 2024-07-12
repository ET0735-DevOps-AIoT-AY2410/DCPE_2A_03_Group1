########################################################
# READ ME READ ME READ ME READ ME READ ME
# dependency library: requests
# To send a notification, use sendNotif(type, location)
    # type must be "fire" or "help"
    # location must be a string
########################################################
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
        "help" : "URGENT HELP NEEDED"
    }
    message = f"{msgHeader_dict[type]}\nLocation: {location}"
    url_sendMessage = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatID}&text={message}"
    print(requests.get(url_sendMessage).json()) # sends msg
    print("Message Sent")

if __name__ == "__main__":
    while(True):
        main()    