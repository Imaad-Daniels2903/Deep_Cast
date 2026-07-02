from prompt_toolkit import PromptSession, prompt
import utils.email_tools as et

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
                            methods = ["yagmail", "oauth"]
                            method = ""

                            print("Choose one of these methods: yagmail, oauth")
                            while method not in methods:
                               method = input('method: ') 
                            
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