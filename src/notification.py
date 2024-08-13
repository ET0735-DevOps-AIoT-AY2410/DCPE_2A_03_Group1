from threading import Thread
import requests # for telegram bot 
import smtplib # smtp service, for emailing
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
    locationInput = input('What is the location? ')
    if (int(selectionInput) == 1): 
        sendNotif("fire", locationInput)
    elif (int(selectionInput) == 2):
        sendNotif("help", locationInput)
    elif (int(selectionInput) == 3):
        sendNotif("false_alarm", locationInput)
    else:
        print("ERROR: Invalid Selection")

def sendNotif(type, location): # calls detached thread
    global messageContent_dict
    global messageHeader_dict
    print("Sending Notification and Email...")
    Thread(target=thread_sendNotif, args=(type, location)).start()

def thread_sendNotif(type, location):
    telegramNotif(type, location)
    emailNotif(type, location)

def telegramNotif(type, location): # sends message via telegram
    token = "7317584084:AAFmG-5ZwZwNfU8fAiypMp56qsEmmEDKy00"
    chatID = "5896827510"
    message = f"{messageContent_dict[type]}\nLocation: {location}"
    url_sendMessage = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatID}&text={message}"

    requests.get(url_sendMessage).json() # sends msg
    print(f"{type} notification sent to SCDF_Bot on Telegram!")

def emailNotif(type, location):
    from_email = 'devops_group1_notifsystem@outlook.com'
    to_email = 'bryanong.23@ichat.sp.edu.sg'
    password = 'devops_group1'

    subject = messageHeader_dict[type]
    email_content = f"Dear SCDF,\n    {messageContent_dict[type]}\n    Location: {location}"
    
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