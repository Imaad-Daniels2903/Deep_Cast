from prompt_toolkit import PromptSession, prompt
from utils import email_valid

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
                            
                            valid = False
                            while not valid : 
                                caster_email = prompt('From : ')
                                valid = email_valid.is_valid_email(caster_email)
                                
                                reciever_email = prompt('To : ')
                                valid = email_valid.is_valid_email(reciever_email)
                            
                            print(f"sent bait to {reciever_email} from {caster_email}")
                        
                    
                except KeyboardInterrupt:
                    # Handles Ctrl+C gracefully
                    continue
                
                except EOFError:
                    # Handles Ctrl+D gracefully
                    break

# def main() :
#     t = terminal()
#     t.start()

# if __name__ == "__main__" :
#     main()