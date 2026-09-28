from prompt_toolkit import PromptSession, prompt
import deep_cast.utils.email_tools as et

class terminal() :

    def start(self) :
        # Create the session once outside the loop
            session = PromptSession()
        
            print("Type 'exit' or 'quit' to end.")
            
            while True:
                try:
                    # Use session.prompt instead of standard prompt
                    text = session.prompt('DeepCast ❯ ')
                    
                    match(text.strip().lower()) :
                        case 'quit' | 'exit' :
                            break
                        
                        case 'gophish' :
                            print("It's time to go Phishing!")
                            methods = ["yagmail", "oauth", "sendgrid", "smtplib"]
                            method = ""

                            print("""
Choose one of these methods: 
[1] yagmail
[2] oauth 
[3] sendgrid
[4] smtplib
                                """)
                            
                            while method not in methods:
                                method = input('method: ')
                                if method not in methods and method.isdigit():
                                    match(int(method)) :
                                        case 1 | 2 | 3 | 4:
                                            method = methods[int(method) - 1]

                                        case _ :
                                            print("incorrect input")
                            
                            sender = self.get_sender(method)

                            print("sender loaded successfully")
                            
                            valid = False
                            caster_email = ""
                            reciever_email = ""
                            
                            while not valid : 
                                caster_email = prompt('From : ')
                                valid = et.is_valid_email(caster_email)
                                
                                reciever_email = prompt('To : ')
                                valid = et.is_valid_email(reciever_email)
                            
                            print(f"sent bait to {reciever_email} from {caster_email}")
                        
                    
                except KeyboardInterrupt:
                    # Handles Ctrl+C gracefully
                    continue
                
                except EOFError:
                    # Handles Ctrl+D gracefully
                    break

    def get_sender(self, method: str) :
        sender = et.sender(method).create_sender()
        return sender

# def main() :
#     t = terminal()
#     t.start()

# if __name__ == "__main__" :
#     main()