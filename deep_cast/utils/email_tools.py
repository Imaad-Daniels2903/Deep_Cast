import re
from abc import ABC, abstractmethod
from senders import oAuth, sendgrid, smtplib, yagmail

# A robust, standard email regex
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def is_valid_email(email: str) -> bool:
    # re.match checks from the start of the string
    if re.match(email_regex, email):
        return True
    return False

def send_email(email: str) :
    pass


class sender(ABC) :

    def __init__(self, method: str) -> None :
        self.method = method

    @abstractmethod
    def init_sender(self) :
        pass

    @abstractmethod
    def send(self) :
        pass


    def create_sender(self) :
        match(self.method.lower()) :
            case "oauth" : 
                return yagmail

            case "stmplib" :
                pass

            case "yagmail" :
                pass

            case "sendgrid" :
                pass