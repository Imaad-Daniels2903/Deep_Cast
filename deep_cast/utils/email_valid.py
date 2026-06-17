import re

# A robust, standard email regex
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def is_valid_email(email):
    # re.match checks from the start of the string
    if re.match(email_regex, email):
        return True
    return False