import re
import yagmail as yg
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os

# A robust, standard email regex
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def is_valid_email(email: str) -> bool:
    # re.match checks from the start of the string
    if re.match(email_regex, email):
        return True
    return False

def send_email(email: str) :
    pass


class sender() :

    def __init__(self, method: str) -> None :
        self.method = method

    def create_sender(self) :
        match(self.method.lower()) :
            case "oauth" : 
                return o_auth().init_sender()

            case "stmplib" :
                return 

            case "yagmail" :
                sender_email = input('sender email: ')
                app_pass = input('app password: ')
                return ya_gmail().init_sender(sender_email, app_pass)

            case "sendgrid" :
                pass
            
            
class ya_gmail() :
    def init_sender(self, sender: str = "", app_password: str = ""):
        self.sender = sender
        self.app_password = app_password
        
        self.y = yg.SMTP(sender, app_password)
        
    
    def send(self, recipient: str, subject: str, body: str):
        self.y.send(recipient, subject, body)


class o_auth() :
    
    def init_sender(self):
        SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
        
        creds = None

        # Load saved token if it exists
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)

        # If no valid token, do the OAuth login flow
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())          # silently refreshgb
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                creds = flow.run_local_server(port=0)  # opens browser for login
            with open("secrets/token.json", "w") as f:
                f.write(creds.to_json())           # save for next time

        return build("gmail", "v1", credentials=creds)
    
    def send(self):
        pass


class smtp_lib(sender) :
    def init_sender(self):
        return super().init_sender()
    
    def send(self):
        return super().send()


class send_grid(sender) :
    def init_sender(self):
        return super().init_sender()
    
    def send(self):
        return super().send()
