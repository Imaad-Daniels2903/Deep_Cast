import os
import re
from encryption import cipher
from dotenv import load_dotenv, set_key


def promptInput(promptMessage : str = "") -> str :
    return input(promptMessage)

def is_valid_email(email : str) -> bool :
    EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    return bool(re.match(EMAIL_REGEX, email))
        
def add_to_env(key : str, value : str) :
    dotenv_path = ".env"

    if not os.path.exists(dotenv_path):
        open(dotenv_path, "w").close()

    set_key(dotenv_path, key, value)

    load_dotenv(dotenv_path, override=True)


def main():
    print("""
==================================================
        WELCOME TO THE DEEPCAST SETUP WIZARD
==================================================

To ensure DeepCast functions properly, you need to configure your
email credentials. These details allow the application to send emails
as intended.

Please follow the instructions below and make sure your credentials 
are entered correctly. If you enter incorrect information or experience
a failure, you can update your settings at any time.
""")  
    
app_password = input("""
An App Paswword is required for the yagmail and smtplib methods. Which also
requires 2FA(two factor authentication) to be enabled. If that has not been
established it is adviced for the functionality of this application to do so

Enter App Password :
""")

api_url = input("""
An API url is required to use the sendgrid method
""")

    
if __name__ == "__main__":
    main()