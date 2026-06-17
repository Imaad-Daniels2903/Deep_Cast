from prompt_toolkit import PromptSession

class terminal() :

    def start(self) :
        # Create the session once outside the loop
            session = PromptSession()
        
            print("Type 'exit' or 'quit' to end.")
            
            while True:
                try:
                    # Use session.prompt instead of standard prompt
                    text = session.prompt('MyApp ❯ ')
                    
                    if text.strip().lower() in ['exit', 'quit']:
                        break
                        
                    print(f"You typed: {text}")
                    
                except KeyboardInterrupt:
                    # Handles Ctrl+C gracefully
                    continue
                except EOFError:
                    # Handles Ctrl+D gracefully
                    break

def main() :
    t = terminal()
    t.start()

if __name__ == "__main__" :
    main()