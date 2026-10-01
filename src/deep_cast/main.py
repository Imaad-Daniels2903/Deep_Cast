import deep_cast.setup_wizard as setup_wizard
import os
from deep_cast.ui import cli
import keyring

def cli_entry() :
    if keyring.get_password("deep_cast", "EMAIL") is None :
        setup_wizard.main()
        
    t = cli.terminal()
    t.start()
    
    
if __name__ == "__main__" : 
    cli_entry()