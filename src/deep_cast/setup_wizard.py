import os
import re
import keyring
# from encryption import cipher
from deep_cast.utils.email_tools import is_valid_email


def promptInput(promptMessage : str = "") -> str :
    return input(promptMessage)

    return bool(re.match(EMAIL_REGEX, email))
        
def add_to_keyring(key : str, value : str) :
    keyring.set_password("deep_cast", key, value)
    
def make_hyperlink(url: str, text: str) -> str:
    # \033]8;; creates the link start, \033\ ends the header
    # \033]8;;\033\ terminates the link anchor
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"


def main():
    print("""
==============================================================================
                    WELCOME TO THE DEEPCAST SETUP WIZARD
==============================================================================

To ensure DeepCast functions properly, you need to configure your
email credentials. These details allow the application to send emails
as intended.

Please follow the instructions below and make sure your credentials 
are entered correctly. If you enter incorrect information or experience
a failure, you can update your settings at any time.
""")
    
    app_password = input("""
==============================================================================
                            APP PASSWORD SETUP
==============================================================================

An App Password is required for the yagmail and smtplib methods. Which also
requires 2FA(two factor authentication) to be enabled. If that has not been
established go to the App Password section in the README and follow the instructions.

Enter App Password : """)
    if not app_password.strip :
        add_to_keyring("APP_PASSWORD", "N/A")
    
    else :
        add_to_keyring("APP_PASSWORD", app_password)
    

    api_url = input("""
==============================================================================
                                API URL SETUP
==============================================================================

An API url is required to use the sendgrid method and it is also required that
you have a sendgrid to acquire the API URL. If you do not have an account 
follow """ + make_hyperlink("https://sendgrid.com", "this link ") + """and create an account then enter API url below. If you do not
want to use this method press enter to continue.

Enter API url: """)
    if not api_url.strip :
        add_to_keyring("API_URL", "N/A")

    else :
        add_to_keyring("API_URL", api_url)
        

    email = input("""
==============================================================================
                                EMAIL SETUP
==============================================================================

This will be the email address use to send out everything and an be changed at a later stage.

Enter API url: """)
    while not is_valid_email(email.lower().strip()) :
        email = input('Email is not valid, please try again: ')
        
    add_to_keyring("EMAIL", email)     

    
if __name__ == "__main__":
    main()