import os
import re
# from encryption import cipher
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
        add_to_env("APP_PASSWORD", "N/A")
    
    else :
        add_to_env("APP_PASSWORD", app_password)
    

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
        add_to_env("API_URL", "N/A")

    else :
        add_to_env("API_URL", api_url)

    
if __name__ == "__main__":
    main()