import json
from threading import Thread
import requests # for telegram bot 
import smtplib # smtp service, for emailing
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load configuration from JSON file
with open('notif_config.json', 'r') as config_file:
    config = json.load(config_file)

messageHeader_dict = { # title text dictionary
    "fire" : "FIRE ALARM ACTIVATED",
    "help" : "URGENT HELP NEEDED BY SCDF",
    "false_alarm" : "FIRE ALARM WAS FALSE"
}
messageContent_dict = { # content text dictionary
    "fire" : "FIRE DETECTED. Fire Alarm has been Activated",
    "help" : "URGENT HELP NEEDED. SOS Switch has been Activated",
    "false_alarm" : "FALSE ALARM. Fire Alarm has been Deactivated"
}

def debug(): # for testing notifications ONLY, not to be used by other code
    selectionInput = input('1: Fire\n2: Help needed\n3: False Alarm\nWhat is the situation? ')
    if (int(selectionInput) == 1): 
        sendNotif("fire")
    elif (int(selectionInput) == 2):
        sendNotif("help")
    elif (int(selectionInput) == 3):
        sendNotif("false_alarm")
    else:
        print("ERROR: Invalid Selection")

def sendNotif(type): # calls detached thread
    global messageContent_dict
    global messageHeader_dict
    print("Sending Notification and Email...")
    Thread(target=thread_sendNotif, args=(type,)).start()

def thread_sendNotif(type):
    telegramNotif(type)
    emailNotif(type)

def telegramNotif(type): # sends message via telegram
    token = "7317584084:AAFmG-5ZwZwNfU8fAiypMp56qsEmmEDKy00"
    chatID = "5896827510"
    message = f"{messageContent_dict[type]}\nLocation: {config['system_location']}"
    url_sendMessage = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatID}&text={message}"

    requests.get(url_sendMessage).json() # sends msg
    print(f"{type} notification sent to SCDF_Bot on Telegram!")

def emailNotif(type):
    from_email = 'devops_group1_notifsys@outlook.com'
    to_email = config['recipient_email']
    password = 'group1_devops'

    subject = messageHeader_dict[type]
    email_content = f"Dear SCDF,\n    {messageContent_dict[type]}\n    Location: {config['system_location']}"
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(email_content, 'plain'))

    server = smtplib.SMTP('smtp.office365.com', 587) # sender is outlook email
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    print(f"{type} email sent to {to_email}!")
    server.quit()

if __name__ == "__main__":
    debug()  