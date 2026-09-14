# import encryption.cipher

def getAppPassword() :
    message = "Enter App Password :"
    print(promptInput(message))
    
def getApi() : 
    message = "Enter API URL :"
    print(promptInput(message))
    
def getEmail() :
    message = "Enter Phishing email :"
    print(promptInput(message))
    
def main():
    getAppPassword()
    getApi()
    getEmail()    
    
def promptInput(promptMessage : str = "") -> str :
    return input(promptMessage)
    
if __name__ == "__main__":
    main()